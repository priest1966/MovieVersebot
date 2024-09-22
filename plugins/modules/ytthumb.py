import os
import time
import ytthumb
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["ytthumb"]))
async def send_thumbnail(bot, update):
    message = await update.reply_text(
        text="Generating Thumbnail ...",
        disable_web_page_preview=True,
        quote=True
    )
    try:
        if " | " in update.text:
            video = update.text.split(" | ", -1)[0]
            quality = update.text.split(" | ", -1)[1]
        else:
            video = update.text
            quality = "sd"
        thumbnail = ytthumb.thumbnail(
            video=video,
            quality=quality
        )
        await update.reply_photo(
            photo=thumbnail,
            quote=True
        )
        await message.delete()
    except Exception as error:
        await message.edit_text(
            text="Incomplete Command\n\n➥  Give me YT video link with the command !\n\n Example:\n\n`/ytthumb https://youtu.be/9-YmVW4HBPU`",
            disable_web_page_preview=True
        )
