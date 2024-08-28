from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from info import *
from urllib.parse import quote_plus
from util.file_properties import get_name, get_hash, get_media_file_size
from util.human_readable import humanbytes
import humanize
import asyncio
import random

"""add time im seconds for waitingwaiting before delete 
1min=60, 2min=60×2=120, 5min=60×5=300"""
SECONDS = int(os.getenv("SECONDS", "10"))

@Client.on_message(filters.private & filters.command("stream"))
async def stream_start(client, message):
    if STREAM_MODE == False:
        return 
    msg = await client.ask(message.chat.id, "**ʙʀᴏ ɴᴏᴡ sᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛᴏ ɢᴇᴛ sᴛʀᴇᴀᴍ ᴀɴᴅ ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ**")
    if not msg.media:
        return await message.reply("**ʙʀʀᴜʜ ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴍᴇ sᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ.**")
    if msg.media in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.DOCUMENT]:
        file = getattr(msg, msg.media.value)
        filename = file.file_name
        filesize = humanize.naturalsize(file.file_size) 
        fileid = file.file_id
        user_id = message.from_user.id
        username =  message.from_user.mention 

        log_msg = await client.send_cached_media(
            chat_id=LOG_CHANNEL,
            file_id=fileid,
        )
        fileName = {quote_plus(get_name(log_msg))}
        lazy_stream = f"{URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        lazy_download = f"{URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
 
        await log_msg.reply_text(
            text=f"•• ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ꜰᴏʀ ɪᴅ #{user_id} \n•• ᴜꜱᴇʀɴᴀᴍᴇ : {username} \n\n•• ғɪʟᴇ ɴᴀᴍᴇ : {fileName}",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("• ᴅᴏᴡɴʟᴏᴀᴅ", url=lazy_download),  # we download Link
                                                InlineKeyboardButton('sᴛʀᴇᴀᴍ •', url=lazy_stream)]])  # web stream Link
        )
        rm=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• sᴛʀᴇᴀᴍ", url=lazy_stream),
                    InlineKeyboardButton('ᴅᴏᴡɴʟᴏᴀᴅ •', url=lazy_download)
                ]
            ] 
        )
        msg_text = """<i><u>ʙʀᴏ ʜᴇʀᴇ's ʏᴏᴜʀ ɢᴇɴᴇʀᴀᴛᴇᴅ !</u></i>\n\n<b>Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n\n<b>Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n\n<b>Dᴏᴡɴʟᴏᴀᴅ :</b> <i>{}</i>\n\n<b>ᴡᴀᴛᴄʜ  :</b> <i>{}</i>\n\n<b>Nᴏᴛᴇ : ʟɪɴᴋ ᴡᴏɴ'ᴛ ᴇxᴘɪʀᴇ ᴛɪʟʟ ɪ ᴅᴇʟᴇᴛᴇ</b>\n\nBaka! Link will be deleted After 1 minutes. Save them to the Saved Message now!.</b>"""

        lazy_d = await message.reply_text(text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(msg)), lazy_download, lazy_stream), quote=True, disable_web_page_preview=True, reply_markup=rm)
        await asyncio.sleep(60)
        await lazy_d.delete()
