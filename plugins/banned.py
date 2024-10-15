from pyrogram import Client, filters
from utils import temp
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from database.users_chats_db import db
from info import SUPPORT_CHAT


# Filter to check if user is banned
async def banned_users(_, __, message: Message):
    return message.from_user is not None and message.from_user.id in temp.BANNED_USERS

banned_user = filters.create(banned_users)


# Filter to check if chat/group is disabled
async def disabled_chat(_, __, message: Message):
    return message.chat is not None and message.chat.id in temp.BANNED_CHATS

disabled_group = filters.create(disabled_chat)


# Handle banned users in private chats
@Client.on_message(filters.private & banned_user & filters.incoming)
async def ban_reply(bot, message: Message):
    ban = await db.get_ban_status(message.from_user.id)
    await message.reply(f"Sorry, you are banned from using me.\nBan Reason: {ban['ban_reason']}")


# Handle disabled chats in groups
@Client.on_message(filters.group & disabled_group & filters.incoming)
async def grp_bd(bot, message: Message):
    buttons = [[InlineKeyboardButton('Support', url='https://t.me/movieverse_discussion_2')]]
    reply_markup = InlineKeyboardMarkup(buttons)

    # Get group ban reason from the database
    group_info = await db.get_chat(message.chat.id)

    # Send notification to the group and try to pin it
    try:
        notification = await message.reply(
            text=f"ᴄʜᴀᴛ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ\n\nᴍʏ ᴀᴅᴍɪɴꜱ ʜᴀꜱ ʀᴇꜱᴛʀɪᴄᴛᴇᴅ ᴍᴇ ꜰʀᴏᴍ ᴡᴏʀᴋɪɴɢ ʜᴇʀᴇ !\n"
                 f"ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ɪᴛ ᴄᴏɴᴛᴀᴄᴛ ꜱᴜᴘᴘᴏʀᴛ.\nReason: <code>{group_info['reason']}</code>.",
            reply_markup=reply_markup
        )
        await notification.pin()  # Attempt to pin the notification message
    except Exception as e:
        print(f"Failed to pin message: {e}")

    # Leave the restricted chat
    await bot.leave_chat(message.chat.id)
