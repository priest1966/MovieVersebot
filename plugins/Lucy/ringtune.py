import os
import logging
from pyrogram import Client, filters, enums
import requests
import json
from info import LOG_CHANNEL


@Client.on_message(filters.command("ringtune"))
async def music(client, message):

    query = " ".join(message.command[1:])


    if not query:
        await client.send_message(message.chat.id, "ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ sᴏɴɢ ɴᴀᴍᴇ ᴛᴏ sᴇᴀʀᴄʜ. ᴜsᴀɢᴇ: /ringtune (song_name) or (song_name + Artist_name)")
        return

    try:
  
        response = requests.get(f"https://api.deezer.com/search?q={query}")


        response.raise_for_status()


        result = response.json()


        if "data" not in result or not result["data"]:
            await client.send_message(message.chat.id, "ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ {query}.")
            return

        song = result["data"][0]

 
        song_info = {
            "artist": song["artist"]["name"],
            "title": song["title"],
            "duration": song["duration"],
            "preview_url": song["preview"],
        }


        await client.send_message(message.chat.id, f"ʜᴇʏ {message.from_user.mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ {query}\n\nᴀʀᴛɪsᴛ: {song_info['artist']}\nᴛɪᴛʟᴇ: {song_info['title']}\nᴅᴜʀᴀᴛɪᴏɴ: {song_info['duration']} sᴇᴄᴏɴᴅs\n\nʏᴏᴜ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜɪs sᴏɴɢ ғʀᴏᴍ ᴄʜʀᴏᴍᴇ: {song_info['preview_url']}")


        await client.send_chat_action(message.chat.id, "upload_audio")

  
        if message.reply_to_message and message.reply_to_message.media:

            await client.send_audio(message.chat.id, song_info['preview_url'], title=song_info['title'], performer=song_info['artist'], reply_to_message_id=message.reply_to_message.id)
        else:

            await client.send_audio(message.chat.id, song_info['preview_url'], title=song_info['title'], performer=song_info['artist'], reply_to_message_id=message.id)
    except requests.RequestException as e:

        logging.error(f"Error fetching song information: {e}")
        await client.send_message(message.chat.id, "An error occurred while fetching the song information. Please try again later.")
        await client.send_message(LOG_CHANNEL, text=f"#ʀɪɴɢᴛᴜɴᴇ\nʀᴇǫᴜᴇsᴛᴇᴅ ғʀᴏᴍ {message.from_user.mention}\nʀᴇǫᴜᴇsᴛ ɪs {query}")
