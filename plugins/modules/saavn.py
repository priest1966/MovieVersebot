# Spotify-Downloader

### This download from saavn.me an unofficial api
from pyrogram import Client,filters, enums
import requests,os,wget
# from info import GRP_LNK, REQST_CHANNEL, SUPPORT_CHAT_ID, ADMINS

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from info import LOG_CHANNEL
BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ʟɪɴᴋs', url='https://t.me/movieversepremium/7')]])
A = """{} with user id:- {} used /saavn command."""
B = """{} with user id:- {} used /vsaavn command."""

# API = "https://apibu.herokuapp.com/api/y-images?query="

START_MESSAGE = """
ʜᴇʟʟᴏ <a href='tg://settings'>ᴛʜᴀɴᴋ ʏᴏᴜ</a>
<i>You can get the song you want only if you ask in the group without spelling it wrong...!! \n\n



For Example :- 
/ssong Alone = saavan mp3 song
/svideo Alone =  saavan video song
/ysong Alone =   youtube mp3 song
/yvideo Alone = youtube mp4 song
/saavan Alone English
/vmp4 Alone Undo
/ysong Alone Song
/yvideo Alone New</a>
Owner Name :- {}
Group Name :- {}
"""







@Client.on_message(filters.command('svideo') & filters.text)
async def video(client, message): 
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply("/svideo requires an argument.")
    if args.startswith(" "):
        await message.reply("/svideo requires an argument.")
        return ""
    pak = await message.reply('Downloading...')
    try:
        r = requests.get(f"https://saavn.me/search/songs?query={args}&page=1&limit=1").json()
    except Exception as e:
        await pak.edit(str(e))
        return
    r = requests.get(f"https://saavn.me/search/songs?query={args}&page=2&limit=2").json()
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
#   album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp3", "mp4")
    os.rename(file, ffile)
    buttons = [[
        InlineKeyboardButton("ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴊᴏɪɴ ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ", url="https://t.me/movieverse_discussion_2")
    ]]                           
    await message.reply_video(
    video=ffile, caption=f"[{sname}]({r['data']['results'][0]['url']}) - from <b>[MovieVerse](https://t.me/movieversepremium)</b>",thumb=thumbnail,
    reply_markup=InlineKeyboardMarkup(buttons)
)
    await message.reply_text(text="Download flac song @Spotiverse_bot")
    os.remove(ffile)
    os.remove(thumbnail)
    await pak.delete()

    await client.send_message(LOG_CHANNEL, B.format(message.from_user.mention, message.from_user.id)) 
    


#    await client.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
        

@Client.on_message(filters.command('ssong') & filters.text)
async def song(client, message):
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply("/ssong requires an argument.")
    if args.startswith(" "):
        await message.reply("/ssong requires an argument.")
        return ""
    pak = await message.reply('Downloading...')
    try:
        r = requests.get(f"https://saavn.me/search/songs?query={args}&page=1&limit=1").json()
    except Exception as e:
        await pak.edit(str(e))
        return
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
  #  album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp4", "mp3")
    os.rename(file, ffile)
    await pak.edit('Uploading...')
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers,caption=f"[{sname}]({r['data']['results'][0]['url']}) - from saavn ",thumb=thumbnail)
    os.remove(ffile)
    os.remove(thumbnail)
    await pak.delete()
    await client.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
    

@Client.on_message(filters.command("song") & filters.group) 
async def r_message(client, message):
    mention = message.from_user.mention
    buttons = [[
        InlineKeyboardButton('Join Group', url=f'https://t.me/movieverse_discussion_2')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(START_MESSAGE.format(message.from_user.mention, message.chat.title),
    protect_content=True,
    reply_markup=reply_markup, 
    parse_mode=enums.ParseMode.HTML
    )
