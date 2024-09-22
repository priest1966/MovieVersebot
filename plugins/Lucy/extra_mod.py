import requests
from pyrogram import Client, filters, enums
from info import BOT_USERNAME
import time
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
@Client.on_message(filters.command("mahadev"))
async def Mahadev(bot, message):
    try:
        
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO) 
        response = requests.get(f'https://mukesh-api.vercel.app/mahadev') 
        x=response.json()["results"]
            
        await message.reply_photo(photo=x,caption=f" \nᴘᴏᴡᴇʀᴇᴅ ʙʏ : <b>[MovieVerse](https://t.me/movieversepremium)</b> ", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
@Client.on_message(filters.command("uselessfact"))
async def uselessa_fact(bot, message):
    try:
        
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING) 
        response = requests.get(f'https://mukesh-api.vercel.app/uselessfact') 
        x=response.json()["results"]
            
        await message.reply_text(x, parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
