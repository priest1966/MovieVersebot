import logging
import asyncio
import re
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import (
    ChannelInvalid, ChatAdminRequired, UsernameInvalid, UsernameNotModified
)
from info import ADMINS, INDEX_REQ_CHANNEL as LOG_CHANNEL
from database.ia_filterdb import save_file
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
lock = asyncio.Lock()

@Client.on_callback_query(filters.regex(r'^index'))
async def index_files(bot, query):
    try:
        if query.data.startswith('index_cancel'):
            temp.CANCEL = True
            return await query.answer("Cancelling Indexing")
        
        # Extract information from the callback data
        _, action, chat, lst_msg_id, from_user = query.data.split("#")

        if action == 'reject':
            await query.message.delete()
            await bot.send_message(
                int(from_user),
                f'Your submission for indexing {chat} has been declined by our moderators.',
                reply_to_message_id=int(lst_msg_id)
            )
            return

        if lock.locked():
            return await query.answer('Wait until the previous process completes.', show_alert=True)

        msg = query.message
        await query.answer('Processing...', show_alert=True)

        # Notify non-admin users that their request has been accepted
        if int(from_user) not in ADMINS:
            await bot.send_message(
                int(from_user),
                f'Your submission for indexing {chat} has been accepted by our moderators and will be added soon.',
                reply_to_message_id=int(lst_msg_id)
            )
        await msg.edit(
            "Starting Indexing",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton('Cancel', callback_data='index_cancel')]]
            )
        )

        # Try converting chat ID to integer; handle both username and integer chat ID formats
        try:
            chat = int(chat)
        except ValueError:
            pass  # Use chat as string if it can't be converted to int

        # Start the indexing process
        await index_files_to_db(int(lst_msg_id), chat, msg, bot)
    except Exception as e:
        logger.error(f"Error in index_files: {e}")
        await query.message.reply(f"An error occurred: {e}")

@Client.on_message((filters.forwarded | (filters.regex(r"(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")) & filters.text) & filters.private & filters.incoming)
async def send_for_index(bot, message):
    try:
        if message.text:
            regex = re.compile(r"(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")
            match = regex.match(message.text)
            if not match:
                return await message.reply('Invalid link')

            chat_id = match.group(4)
            last_msg_id = int(match.group(5))

            if chat_id.isnumeric():
                chat_id = int("-100" + chat_id)  # Convert to Telegram private chat ID format

        elif message.forward_from_chat and message.forward_from_chat.type == enums.ChatType.CHANNEL:
            last_msg_id = message.forward_from_message_id
            chat_id = message.forward_from_chat.username or message.forward_from_chat.id
        else:
            return

        # Check if the bot can access the chat
        try:
            await bot.get_chat(chat_id)
        except ChannelInvalid:
            return await message.reply('This may be a private channel/group. Make me an admin to index the files.')
        except (UsernameInvalid, UsernameNotModified):
            return await message.reply('Invalid link specified.')
        except Exception as e:
            logger.error(f"Error fetching chat: {e}")
            return await message.reply(f'Error: {e}')

        try:
            k = await bot.get_messages(chat_id, last_msg_id)
        except Exception:
            return await message.reply('Make sure I am an admin in the channel if the channel is private.')

        if k.empty:
            return await message.reply('This may be a group, and I am not an admin of the group.')

        # Admins can approve indexing immediately
        if message.from_user.id in ADMINS:
            buttons = [
                [InlineKeyboardButton('Yes', callback_data=f'index#accept#{chat_id}#{last_msg_id}#{message.from_user.id}')],
                [InlineKeyboardButton('Close', callback_data='close_data')],
            ]
            reply_markup = InlineKeyboardMarkup(buttons)
            return await message.reply(
                f'Do you want to index this channel/group?\n\nChat ID/Username: <code>{chat_id}</code>\nLast Message ID: <code>{last_msg_id}</code>',
                reply_markup=reply_markup)

        # Create invite link for non-admins
        if isinstance(chat_id, int):
            try:
                link = (await bot.create_chat_invite_link(chat_id)).invite_link
            except ChatAdminRequired:
                return await message.reply('Make sure I am an admin and have permission to invite users.')
        else:
            link = f"@{message.forward_from_chat.username}"

        # Non-admins need approval
        buttons = [
            [InlineKeyboardButton('Accept Index', callback_data=f'index#accept#{chat_id}#{last_msg_id}#{message.from_user.id}')],
            [InlineKeyboardButton('Reject Index', callback_data=f'index#reject#{chat_id}#{message.id}#{message.from_user.id}')],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        await bot.send_message(
            LOG_CHANNEL,
            f'#IndexRequest\n\nBy: {message.from_user.mention} (<code>{message.from_user.id}</code>)\nChat ID/Username: <code>{chat_id}</code>\nLast Message ID: <code>{last_msg_id}</code>\nInvite Link: {link}',
            reply_markup=reply_markup
        )

        await message.reply('Thank you for the contribution. Wait for my moderators to verify the files.')
    except Exception as e:
        logger.error(f"Error in send_for_index: {e}")
        await message.reply(f"An error occurred: {e}")

@Client.on_message(filters.command('setskip') & filters.user(ADMINS))
async def set_skip_number(bot, message):
    try:
        if ' ' in message.text:
            _, skip = message.text.split(" ")
            try:
                skip = int(skip)
            except ValueError:
                return await message.reply("Skip number should be an integer.")
            await message.reply(f"Successfully set SKIP number to {skip}")
            temp.CURRENT = skip
        else:
            await message.reply("Provide a skip number.")
    except Exception as e:
        logger.error(f"Error in set_skip_number: {e}")
        await message.reply(f"An error occurred: {e}")

async def index_files_to_db(lst_msg_id, chat, msg, bot):
    total_files = 0
    duplicate = 0
    errors = 0
    deleted = 0
    no_media = 0
    unsupported = 0

    async with lock:
        try:
            current = temp.CURRENT
            temp.CANCEL = False

            async for message in bot.iter_messages(chat, lst_msg_id, temp.CURRENT):
                if temp.CANCEL:
                    await msg.edit(f"Cancelled!\n\nSaved <code>{total_files}</code> files to the database!\nDuplicate Files: <code>{duplicate}</code>\nDeleted Messages: <code>{deleted}</code>\nNon-Media Messages: <code>{no_media + unsupported}</code> (Unsupported: `{unsupported}`)\nErrors: <code>{errors}</code>")
                    break

                current += 1
                if current % 200 == 0:
                    await asyncio.sleep(20)
                if current % 20 == 0:
                    can = [[InlineKeyboardButton('Cancel', callback_data='index_cancel')]]
                    reply = InlineKeyboardMarkup(can)
                    await msg.edit_text(
                        f"Total messages fetched: <code>{current}</code>\nTotal messages saved: <code>{total_files}</code>\nDuplicate Files: <code>{duplicate}</code>\nDeleted Messages: <code>{deleted}</code>\nNon-Media: <code>{no_media + unsupported}</code> (Unsupported: `{unsupported}`)\nErrors: <code>{errors}</code>",
                        reply_markup=reply
                    )

                if message.empty:
                    deleted += 1
                    continue
                elif not message.media:
                    no_media += 1
                    continue
                elif message.media not in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.AUDIO, enums.MessageMediaType.DOCUMENT]:
                    unsupported += 1
                    continue

                media = getattr(message, message.media.value, None)
                if not media:
                    unsupported += 1
                    continue

                media.file_type = message.media.value
                media.caption = message.caption

                aynav, vnay = await save_file(media)

                if aynav:
                    total_files += 1
                elif vnay == 0:
                    duplicate += 1
                elif vnay == 2:
                    errors += 1

        except Exception as e:
            logger.error(f"Error in index_files_to_db: {e}")
            await msg.reply(f"Error while indexing: {e}")
        
        await msg.edit_text(
            f"Completed!\n\nSaved <code>{total_files}</code> files to the database!\nDuplicate Files: <code>{duplicate}</code>\nDeleted Messages: <code>{deleted}</code>\nNon-Media Messages: <code>{no_media + unsupported}</code> (Unsupported: `{unsupported}`)\nErrors: <code>{errors}</code>"
        )
