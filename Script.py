class script(object):
    START_TXT = """<b><blockquote>Hᴇʟʟᴏ {}, ᴍʏ ɴᴀᴍᴇ <a href=https://t.me/{}>{}</a></blockquote>
    
ɪ ᴀᴍ ʟᴀᴛᴇꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ+└ᴀᴡᴇꜱᴏᴍᴇ ꜰɪʟᴛᴇʀ┘+├ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ┤+☞ᴍᴀɴᴜᴀʟ ꜰɪᴛᴇʀ☜ ᴀɴᴅ ᢵᴄᴜꜱᴛᴏᴍɪᴢᴇᴅ ꜱʜᴏʀᴛɴᴇʀ ꜱᴜᴘᴘᴏʀᴛᢴ ᢾᴀɴᴅ ʙᴇꜱᴛ ᴜɪ ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇᢿ</b>"""
    GSTART_TXT = """<b>ʜᴇʏ {},\n\nɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\nᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/icecube9680_bot">IceCube</a></b>"""
    
    HELP_TXT = """<b>ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ᴀʙᴏᴜᴛ sᴘᴇᴄɪғɪᴄs ᴄᴏᴍᴍᴀɴᴅ!</b>"""

    ABOUT_TXT = """<b><blockquote>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟</blockquote>
ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/MovieVerse_2_bot">MovieVerse Bot</a>
ᴄʀᴇᴀᴛᴏʀ : <a href="https://t.me/icecube9680_bot">IceCube</a>
ʟɪʙʀᴀʀʏ : <a href="https://pyrogram.org/">ᴘʏʀᴏɢʀᴀᴍ</a>
ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a>
ᴅᴀᴛᴀʙᴀꜱᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ : ᴠ4.4.1 [ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs]

 ɪ ᴄᴀɴ ʀᴇꜱᴛʀɪᴄᴛ ᴜꜱᴇʀꜱ.
 ɪ ʜᴀᴠᴇ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏ-ғɪʟᴛᴇʀ ꜱʏꜱᴛᴇᴍ.
 ɪ ᴄᴀɴ ɢʀᴇᴇᴛ ᴜꜱᴇʀꜱ ᴡɪᴛʜ ᴄᴜꜱᴛᴏᴍɪᴢᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.
 ɪ ᴄᴀɴ ʙᴀɴ, ᴍᴜᴛᴇ, ᴋɪᴄᴋ, ᴇᴛᴄ.
 ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ᴍᴏᴅᴜʟᴇs ʟɪᴋᴇ ғɪʟᴇ sᴛᴏʀᴇ, ғᴏɴᴛ, ᴋᴀɴɢ, ᴀɪ ɪᴍᴀɢᴇ ᴀɴᴅ ᴍᴏʀᴇ.

➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴍᴇ.</b>"""

    SUBSCRIPTION_TXT = """
<b>ʀᴇғᴇʀʀᴇ ʏᴏᴜʀ ʟɪɴᴋ ᴛᴏ ʏᴏᴜʀ ғʀɪᴇɴᴅs, ғᴀᴍɪʟʏ, ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢʀᴏᴜᴘ ᴛᴏ ɢᴇᴛ ғʀᴇᴇ ᴘʀᴇᴍɪᴜᴍ ғᴏʀ {}

ʀᴇғᴇʀᴀʟ ʟɪɴᴋ - https://telegram.me/{}?start=MV-{}

ɪғ {} ᴜɴɪǫᴜᴇ ᴜsᴇʀ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜ ʏᴏᴜʀ ʀᴇғᴇʀᴀʟ ʟɪɴᴋ ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴅᴅᴇᴅ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.

ʙᴜʏ ᴘᴀɪᴅ ᴘʟᴀɴ ʙʏ - /plan</b>"""

    SOURCE_TXT = """
<b>ʜᴇʏ,
ᴛʜɪs ɪs MovieVerse,
ᴀɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴀɪ ᴀɴᴅ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴍᴏᴅᴜʟᴇs ʙᴏᴛ.

ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ <a href='https://github.com/pyrogram/pyrogram'>ᴩʏʀᴏɢʀᴀᴍ</a> & <a href='https://github.com/python-telegram-bot/python-telegram-bot'>ᴩʏᴛʜᴏɴ-ᴛᴇʟᴇɢʀᴀᴍ-ʙᴏᴛ</a>  
ᴀɴᴅ ᴜsɪɴɢ ᴀɴᴅ <a href='https://cloud.mongodb.com'>ᴍᴏɴɢᴏ</a> ᴀs ᴅᴀᴛᴀʙᴀsᴇ.

</b>"""

    MAIN_TXT = """
ʜᴇʀᴇ ɪꜱ ʜᴇʟᴘ ᴍᴇɴᴜ
"""

    SPECIAL_TXT = """
ᴄʜᴇᴄᴋ ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴅᴜʟᴇ
"""
    
    CHANNELS = """
<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴜs.

ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ᴀɴʏ ʙᴜɢ ɪɴ ˹MovieVerse˼ ᴏʀ ɪғ ʏᴏᴜ ᴡᴀɴɴᴀ ɢɪᴠᴇ ғᴇᴇᴅʙᴀᴄᴋ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ˼, ᴩʟᴇᴀsᴇ ʀᴇᴩᴏʀᴛ ɪᴛ ᴀᴛ <a href='https://t.me/movieverse_discussion_2'>sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ</a>.</b>"""

    DONATE = """<b>Aʀᴇ ʏᴏᴜ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ʜᴇʟᴘɪɴɢ ᴍʏ ᴄʀᴇᴀᴛᴏʀ ᴡɪᴛʜ ʜɪs ᴇғғᴏʀᴛs ᴛᴏ ᴋᴇᴇᴘ ᴍᴇ ɪɴ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ? Iғ ʏᴇs, Yᴏᴜ'ʀᴇ ɪɴ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴀᴄᴇ. 

Wᴇ ᴇᴍᴘʜᴀsɪsᴇ ᴛʜᴇ ɪᴍᴘᴏʀᴛᴀɴᴄᴇ ᴏғ ɴᴇᴇᴅɪɴɢ ғᴜɴᴅs ᴛᴏ ᴋᴇᴇᴘ MovieVerse ᴜɴᴅᴇʀ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ. Yᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ɪɴ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ᴏғ ᴍᴏɴᴇʏ ᴛᴏ MovieVerse sᴇʀᴠᴇʀs ᴀɴᴅ ᴏᴛʜᴇʀ ᴜᴛɪʟɪᴛɪᴇs ᴡɪʟʟ ᴀʟʟᴏᴡ ᴜs ᴛᴏ sᴜsᴛᴀɪɴ ᴛʜᴇ ʟɪғᴇsᴘᴀɴ ɪɴ ᴛʜᴇ ʟᴏɴɢ ᴛᴇʀᴍ. Wᴇ ᴡɪʟʟ ᴜsᴇ ᴀʟʟ ᴏғ ᴛʜᴇ ᴅᴏɴᴀᴛɪᴏɴs ᴛᴏ ᴄᴏᴠᴇʀ ғᴜᴛᴜʀᴇ ᴇxᴘᴇɴsᴇs ᴀɴᴅ ᴜᴘɢʀᴀᴅᴇs ᴏғ ᴛʜᴇ sᴇʀᴠᴇʀs ᴄᴏsᴛs. Iғ ʏᴏᴜ'ᴠᴇ ɢᴏᴛ sᴘᴀʀᴇ ᴍᴏɴᴇʏ ᴛᴏ ʜᴇʟᴘ ᴜs ɪɴ ᴛʜɪs ᴇғғᴏʀᴛ, Kɪɴᴅʟʏ ᴅᴏ sᴏ ᴀɴᴅ ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ᴄᴀɴ ᴀʟsᴏ ᴍᴏᴛɪᴠᴀᴛᴇ ᴜs ᴋᴇᴇᴘ ʙʀɪɴɢ ᴏɴ ɴᴇᴡ ғᴇᴀᴛᴜʀᴇs.

Yᴏᴜ ᴄᴀɴ ʜᴇʟᴘ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ ᴡɪᴛʜ ᴅᴏɴᴀᴛɪᴏɴs
Upi : movieverse@axl

sᴇɴᴅ ss ʜᴇʀᴇ : @icecube9680_bot</b>"""

    SETTINGS_TXT = """
Hᴇʟᴘ : <b>Sᴇᴛᴛɪɴɢꜱ</b>
    
◈ sᴇᴛᴛɪɴɢs ɪs ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇ ɪɴ ᴛʜɪs ʙᴏᴛ.
◈ ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<b>Nᴏᴛᴇ :</b>
1. ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs.
2. ɪᴛ ᴡᴏʀᴋs ᴏɴʟʏ ᴡʜᴇɴ ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /connect - ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ʙᴏᴛ
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ """

    TELEGRAPH_TXT = """ Hᴇʟᴘ : <b>Tᴇʟᴇɢʀᴀᴘʜ</b>

<b>Nᴏᴛᴇ</b>: ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ᴘᴍꜱ. ᴀʟꜱᴏ ᴄᴀɴ ʙᴇ ᴜꜱᴇ ʙʏ ᴇᴠᴇʀʏᴏɴᴇ.

<b>Cᴏᴍᴍᴀɴᴅs & Usᴀɢᴇ :</b>
• /telegraph - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ 𝟻ᴍʙ"""

    FONT_TXT = """Hᴇʟᴘ : <b>Fᴏɴᴛ</b>

<b>Nᴏᴛᴇ</b>: ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛꜱ ꜱᴛʏʟᴇ, ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ʟɪᴋᴇ ᴛʜɪꜱ ꜰᴏʀᴍᴀᴛ. 

<code>/font Team Netflix</code>"""

    MANUELFILTER_TXT = """Hᴇʟᴘ : <b>Fɪʟᴛᴇʀꜱ</b>
    
◈ ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ.

<b>Nᴏᴛᴇ :</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /filter - ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ
• /filters - ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ
• /del - ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ
• /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)"""

    BUTTON_TXT = """Hᴇʟᴘ : <b>Bᴜᴛᴛᴏɴꜱ</b>
    
◈ ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.

<b>Nᴏᴛᴇ :</b>
𝟷. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
𝟸. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
𝟹. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ

ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ :
<code>[Button Text](buttonurl:https://t.me/movieversepremium)</code>

ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ :
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """Hᴇʟᴘ : <b>Aᴜᴛᴏ Fɪʟᴛᴇʀ</b>
    
<b>Nᴏᴛᴇ :</b> Fɪʟᴇ Iɴᴅᴇx
𝟷. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
𝟸. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
𝟹. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<b>Nᴏᴛᴇ :</b> Aᴜᴛᴏ Fɪʟᴛᴇʀ
𝟷. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
𝟸. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
𝟹. Usᴇ /settings ᴏɴ ʙᴏᴛ's ᴘᴍ ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    
    RULE_TXT = """Group Rules

◈ <b>Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ:</b>
• ᴀᴠᴀᴛᴀʀ 𝟸𝟶𝟶𝟿
• ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ
• ᴀᴠᴀᴛᴀʀ ᴍᴏᴠɪᴇ 
• ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ

◈ <b>Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇs Iɴ ᴛʜɪs Fᴏʀᴍᴀᴛ:</b>
• ᴠɪᴋɪɴɢs S𝟶𝟷
• ᴠɪᴋɪɴɢs S𝟶𝟷E𝟶𝟷
• ᴠɪᴋɪɴɢs S𝟶𝟷 ʜɪɴᴅɪ
• ᴠɪᴋɪɴɢs S𝟶𝟷 ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ 
• ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 𝟷 
• ᴠɪᴋɪɴɢs ᴡᴇʙ sᴇʀɪᴇs 

<b>➙ ᴅᴏɴ'ᴛ ᴅᴏ ᴀɴʏ ꜱᴇʟꜰ ᴘʀᴏᴍᴏᴛɪᴏɴ. 
➙ ᴅᴏɴ'ᴛ ꜱᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏꜰ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ, ᴅᴏᴄᴜᴍᴇɴᴛꜱ, ᴜʀʟ, ᴇᴛᴄ...
➙ ᴅᴏɴ'ᴛ ʀᴇǫᴜᴇꜱᴛ ᴀɴʏ ᴛʜɪɴɢꜱ ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇꜱ, ꜱᴇʀɪᴇꜱ, ᴀɴɪᴍᴀᴛɪᴏɴ, ᴄᴀʀᴛᴏᴏɴ, ᴀɴɪᴍᴇ, ᴋ-ᴅʀᴀᴍᴀ ᴍᴀɴʏ ᴍᴏʀᴇ.</b>

<b>Nᴏᴛᴇ :</b> ᴀʟʟ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀꜰᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇꜱ ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ."""

    CONNECTION_TXT = """Hᴇʟᴘ : <b>Cᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>
    
◈ ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
◈ ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

<b>Nᴏᴛᴇ :</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ /ᴄᴏɴɴᴇᴄᴛ ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /connect  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
• /disconnect  - ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ
• /connections - ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ"""

    EXTRAMOD_TXT = """Hᴇʟᴘ : <b>Exᴛʀᴀ Mᴏᴅᴜʟᴇs</b>
    
<b>Nᴏᴛᴇ :</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /id - ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.
• /info  - ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.
• /imdb  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.
• /search  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ."""

    STICKER_TXT = """<b>yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ꜰɪɴᴅᴀɴy  ꜱᴛɪᴄᴋᴇʀꜱ ɪᴅ.
• ᴜꜱᴀɢᴇ :ᴛᴏ ɢᴇᴛ ꜱᴛɪᴄᴋᴇʀ
 
 ʜᴏᴡ ᴛᴏ ᴜꜱᴇ
◉ Reply To Any Sticker [/stickerid]

/stickerid sticker id of sticker you want to find


</b>"""

    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """Hᴇʟᴘ : <b>Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs</b>
    
◈ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.
    
<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /gfilter - Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.
• /gfilters - Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.
• /delg - Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.
• /delallg - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ."""
    
    FILE_STORE_TXT = """Hᴇʟᴘ : <b>Fɪʟᴇ Sᴛᴏʀᴇ</b>
    
◈ Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /batch - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.
• /link - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.
• /pbatch - ᴊᴜsᴛ ʟɪᴋᴇ <code>/batch</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
• /plink - ᴊᴜsᴛ ʟɪᴋᴇ <code>/link</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ."""


    YTTHUMB = """<b>ʏᴛ-ᴛʜᴜᴍʙ

ʜᴇʟᴘs ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴛʜᴜᴍʙɴᴀɪʟ


ᴜsᴇ ᴛʜɪs ꜰᴏʀᴍᴀᴛ</b> 

<code>/ytthumb https://youtu.be/BqlMwyABHOE</code>"""

    GITHUB = """<b>ɢɪᴛʜᴜʙ ᴅᴇᴛᴀɪʟs -</b>

ᴡɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ, ʏᴏᴜ ᴄᴀɴ ꜰɪɴᴅ ᴏᴜᴛ ᴛʜᴇ ꜰᴜʟʟ ᴅᴇᴛᴀɪʟs ᴏꜰ ᴛʜᴇ ɢɪᴛʜᴜʙ ᴀᴄᴄᴏᴜɴᴛ ᴏꜰ ᴀɴʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴏʀ ᴜsᴇʀs ᴡʜᴏ ʜᴀᴠᴇ ᴀᴄᴄᴏᴜɴᴛ

ᴜsᴇ ᴛʜɪs ꜰᴏʀᴍᴀᴛ

/github phoenix-erotixe
/git : to get github id information
"""

    YTTAGS = """<b>ꜰᴏʀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴛᴀɢs -

ʏᴏᴜ ᴄᴀɴ ꜰɪɴᴅ ᴏᴜᴛ ᴛʜᴇ ᴛᴀɢs ᴏꜰ ᴀɴʏ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴡɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ

➤  ᴄᴏᴍᴍᴀɴᴅs :

/yttags - Reply to a YouTube video</b>"""

    VIDEO_TXT ="""<b>ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ

ʏᴏᴜ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ

➤  ᴄᴏᴍᴍᴀɴᴅs

ᴛʏᴘᴇ /video or /mp4

ᴇxᴀᴍᴘʟᴇ :</b>

<code>/mp4 https://youtu.be/BqlMwyABHOE</code>

<code>/video https://youtu.be/BqlMwyABHOE</code>"""

    REPORT = """<b>ʀᴇᴘᴏʀᴛ

ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ ʀᴇᴘᴏʀᴛ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ᴀ ᴜsᴇʀs ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴs ᴏꜰ ᴛʜᴇ ʀᴇsᴘᴇᴄᴛɪᴠᴇ ɢʀᴏᴜᴘ


➤  ᴄᴏᴍᴍᴀɴᴅs :

/report 𝗈𝗋 @admin - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾).</b>"""


    GEN_PASS = """<b>ᴘᴀssᴡᴏʀᴅ ɢᴇɴᴇʀᴀᴛᴏʀ</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.

- I Will Give The Password Of That Limit.

➤ ᴄᴏᴍᴍᴀɴᴅs :

• /genpassword or /genpw 20

NOTE:
• Only Digits Are Allowed
• Maximum Allowed Digits Till 84 
  (I Can't Generate Passwords Above The Length 84)
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    OPNAI_TXT = """ᴏᴘᴇɴᴀɪ ɪꜱ ᴀ ᴀɪ ꜱʏꜱᴛᴇᴍ ᴛʜᴀᴛ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ꜰɪɴᴅ ᴀɴꜱᴡᴇʀ ᴏꜰ ʏᴏᴜʀ Qᴜᴇꜱᴛɪᴏɴ ᴀɴᴅ ɪᴛ ᴡɪʟʟ ᴏɴʟʏ ᴡᴏʀᴋ ᴏɴ ʙᴏᴛ ᴘᴍ.

ʜᴏᴡ ᴛᴏ ᴜꜱᴇ

/ᴏᴘᴇɴᴀɪ ᴡʜᴀᴛ ɪꜱ ᴀᴘᴘᴇɴᴅ ᴍᴇᴛʜᴏᴅ ɪɴ ᴘʏᴛʜᴏɴ
"""

    KANG = """
Create Own Sticker And Sticker Pack
Send To Image
Reply To Image And Send /kang ᴄᴏᴍᴍᴀɴᴅs
"""

    GROUP_TXT = """
<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴜs.

ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ᴀɴʏ ʙᴜɢ ɪɴ ˹MovieVerse˼ ᴏʀ ɪғ ʏᴏᴜ ᴡᴀɴɴᴀ ɢɪᴠᴇ ғᴇᴇᴅʙᴀᴄᴋ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ˼, ᴩʟᴇᴀsᴇ ʀᴇᴩᴏʀᴛ ɪᴛ ᴀᴛ <a href='https://t.me/movieverse_discussion_2'>sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ</a>.</b>"""

    PURGE_TXT = """<b>ᴘᴜʀɢᴇ
    
ᴅᴇʟᴇᴛᴇ ᴀ ʟᴏᴛ ᴏꜰ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ɢʀᴏᴜᴘs! 
    
 ᴀᴅᴍɪɴ 

◉ /purge :- ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇssᴀɢᴇ​</b>"""

    JSON_TXT = """<b>
ᴊsᴏɴ:

ʙᴏᴛ ʀᴇᴛᴜʀɴs ᴊsᴏɴ ꜰᴏʀ ᴀʟʟ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇs ᴡɪᴛʜ /json

ꜰᴇᴀᴛᴜʀᴇs:

ᴍᴇssᴀɢᴇ ᴇᴅɪᴛᴛɪɴɢ ᴊsᴏɴ
ᴘᴍ sᴜᴘᴘᴏʀᴛ
ɢʀᴏᴜᴘ sᴜᴘᴘᴏʀᴛ

ɴᴏᴛᴇ:

ᴇᴠᴇʀʏᴏɴᴇ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ , ɪꜰ sᴘᴀᴍɪɴɢ ʜᴀᴘᴘᴇɴs ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʙᴀɴ ʏᴏᴜ ꜰʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.​</b>"""

    CARB_TXT = """<b>ʜᴇʟᴩ ꜰᴏʀ ᴄᴀʀʙᴏɴ

ᴄᴀʀʙᴏɴ ɪꜱ ᴀ ꜰᴇᴜᴛᴜʀᴇ ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ᴀꜱ ꜱʜᴏᴡɴ ɪɴ ᴛʜᴇ ᴛᴏᴩ ᴡɪᴛʜ ʏᴏᴜʀ ᴛᴇxᴛꜱ.
ꜰᴏʀ ᴜꜱɪɴɢ ᴛʜᴇ ᴍᴏᴅᴜʟᴇ ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴛʜᴇ ᴛᴇxᴛ ᴀɴᴅ ᴏᴇᴩʟᴀʏ ᴛɪ ɪᴛ ᴡɪᴛʜ  /carbon ᴄᴏᴍᴍᴀɴᴅ ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ᴩᴇᴩᴀʏ ᴡɪᴛʜ ᴛʜᴇ ᴄᴀʀʙᴏɴ ɪᴍᴀɢᴇ

</b>"""

    SONG_TXT = """<b>sᴏɴɢ ᴅᴇᴛᴀɪʟs
sᴏɴɢ sᴇᴀʀᴄʜ ᴠɪᴅᴇᴏ ᴀɴᴅ ᴀᴜᴅɪᴏ

ᴇxᴀᴍᴘʟᴇ -
sᴀᴀᴠɴ sᴏɴɢs ᴄᴏᴍᴍᴀɴᴅ
/ssong ᴀʟᴏɴᴇ 
/svideo ᴀʟᴏɴᴇ

ʏᴛ ᴠɪᴅᴇᴏ ᴄᴏᴍᴍᴀɴᴅ
/ysong ᴀʟᴏɴᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ
/yvideo  ᴀʟᴏɴᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ
</b>"""

    ALIVE = """<b>ᴘɪɴɢ ᴅᴇᴛᴀɪʟs -</b>
/alive Bot Response Test ᴄᴏᴍᴍᴀɴᴅs

/ping Bot Speed Test
"""

    REPO = """<b>ʀᴇᴘᴏ ᴅᴇᴛᴀɪʟs -</b>

ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ɢɪᴛʜᴜʙ's ʀᴇᴘᴏ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴘ ᴏғ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.

/repo : search any repo
/allrepo : get all repo
/downloadrepo : download the repo

ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇ ᴄᴏᴍɪɴɢ sᴏᴏɴ."""

    SHORTNER = """<b>ᴜʀʟ sʜᴏʀᴛɴᴇʀ</b>

ᴛʜɪs ᴍᴏᴅᴜʟᴇ ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ sʜᴏʀᴛ ᴀ ᴜʀʟ ᴀɴᴅ Yᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ᴍᴏɴᴇʏ ғʀᴏᴍ ᴛʜɪs ʙᴏᴛ ᴜɴᴛɪʟ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟɪᴠᴇ.

➤ ᴄᴏᴍᴍᴀɴᴅs:

➪ /short - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌
➪ /shortlinkon - ᴏɴ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
➪ /shortlinkoff - ᴏꜰꜰ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
➪ /shortlink_info - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ.
➪ /set_shortlink - ᴛᴏ sᴇᴛ ᴀ sʜᴏʀᴛʟɪɴᴋ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, use ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ
➪ /set_tutorial - ᴛᴏ sᴇᴛ ᴜᴘ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛᴇɴᴇʀ ᴛᴜᴛᴏʀɪᴀʟ, ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ"""

    LYRICS = """<b>ʟʏʀɪᴄs</b>

ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴘ ᴏғ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ʟʏʀɪᴄs ᴏғ sᴏɴɢs.

➤ ᴄᴏᴍᴍᴀɴᴅ:

➪ /lyrics - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ɢᴇᴛ ʟʏʀɪᴄs."""


    RESTRIC_TXT = """➤ Help: Mᴜᴛᴇ
These are the commands a group admin can use to manage their group mor efficiently.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

ᴘᴏᴡᴇʀᴇᴅ ʙʏ MovieVerse Bot

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""

    GAME_TXT = """<b>Gᴀᴍᴇs</b> 

<b>ɢᴀᴍᴇs  ᴍᴏᴅᴜʟᴇ
    
ᴊᴜsᴛ sᴏᴍᴇ ᴋɪɴᴅ ᴏꜰ ꜰᴜɴ ᴛʜɪɴɢ's
 
𝟣. /dice - ʀᴏʟᴇ ᴛʜᴇ ᴅɪᴄᴇ
𝟤. /Throw ᴏʀ /Dart - ᴛᴏ ᴍᴀᴋᴇ ᴅᴀʀᴛ
3. /Runs - sᴏᴍᴇ ʀᴀɴᴅᴏᴍ ᴅɪᴀʟᴏɢᴜᴇs
4. /Goal ᴏʀ /Shoot - ᴛᴏ ᴍᴀᴋᴇ ᴀ ɢᴏᴀʟ ᴏʀ sʜᴏᴏᴛ
5. /luck ᴏʀ /cownd - sᴘɪɴ ᴀɴᴅ ᴛʀʏ ʏᴏᴜʀ ʟᴜᴄᴋ</b>"""

    CC_TXT = """
<b>HELP: CC Tools

Credit Card stuffs being easy with CC Module!

USAGE:
➢ /sk - Check if stripe key is live or not.
➢ /bin - Check if given bin is valid or not.
➢ /fake - Generate random fake user details.
➢ /gen - Generate random credit cards info.
➢ /cc - Generate random credit cards.

NOTE:
• Lucy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.</b>"""

    ANIME_TXT = """
<b>Get information about animes, manga and characters!

USAGE:
➢ /neko [-n] - Get random neko picture (-n for nsfw).
➢ /waifu [-n] - Get random waifu picture (-n for nsfw).
➢ /anime [name] - Get the information about the anime.
➢ /manga [name] - Get the information about the manga.
➢ /hentai [name] - Get and read the hentai manga (nsfw).
➢ /hentai [-r] - Get random hentai manga to read (nsfw).
➢ /aninews - Get latest anime news from myanimelist.net.
➢ /aniquote - Get awesome random anime quotes everytime.
➢ /character [name] - Get the information about the character.

NOTE:
• Lucy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.</b>"""

    FSUB_TXT = """
<b>Force members to join channel before writing on chat!

USAGE:
➢ /fsub - Get the current status.
➢ /fsub [off] - Disable forcesub in the chat.
➢ /fsub [channel id/ username] - Setup forcesub channel.
➢ /fsub [clear] - Unmute all members who are muted by me.

NOTE:
• Lucy should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.</b>"""

    DONATION_TXT = """<b>donation</b> 

<b>ᴀʀᴇ ʏᴏᴜ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ʜᴇʟᴘɪɴɢ ᴍʏ ᴄʀᴇᴀᴛᴏʀ ᴡɪᴛʜ ʜɪs ᴇғғᴏʀᴛs ᴛᴏ ᴋᴇᴇᴘ ᴍᴇ ɪɴ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ? Iғ ʏᴇs, Yᴏᴜ'ʀᴇ ɪɴ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴀᴄᴇ. 

ᴡᴇ ᴇᴍᴘʜᴀsɪsᴇ ᴛʜᴇ ɪᴍᴘᴏʀᴛᴀɴᴄᴇ ᴏғ ɴᴇᴇᴅɪɴɢ ғᴜɴᴅs ᴛᴏ ᴋᴇᴇᴘ MovieVerse ʙᴏᴛ ᴜɴᴅᴇʀ ᴀᴄᴛɪᴠᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ. ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ɪɴ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ᴏғ ᴍᴏɴᴇʏ ᴛᴏ MovieVerse ʙᴏᴛ sᴇʀᴠᴇʀs ᴀɴᴅ ᴏᴛʜᴇʀ ᴜᴛɪʟɪᴛɪᴇs ᴡɪʟʟ ᴀʟʟᴏᴡ ᴜs ᴛᴏ sᴜsᴛᴀɪɴ ᴛʜᴇ ʟɪғᴇsᴘᴀɴ ɪɴ ᴛʜᴇ ʟᴏɴɢ ᴛᴇʀᴍ. ᴡᴇ ᴡɪʟʟ ᴜsᴇ ᴀʟʟ ᴏғ ᴛʜᴇ ᴅᴏɴᴀᴛɪᴏɴs ᴛᴏ ᴄᴏᴠᴇʀ ғᴜᴛᴜʀᴇ ᴇxᴘᴇɴsᴇs ᴀɴᴅ ᴜᴘɢʀᴀᴅᴇs ᴏғ ᴛʜᴇ sᴇʀᴠᴇʀs ᴄᴏsᴛs. Iғ ʏᴏᴜ'ᴠᴇ ɢᴏᴛ sᴘᴀʀᴇ ᴍᴏɴᴇʏ ᴛᴏ ʜᴇʟᴘ ᴜs ɪɴ ᴛʜɪs ᴇғғᴏʀᴛ, Kɪɴᴅʟʏ ᴅᴏ sᴏ ᴀɴᴅ ʏᴏᴜʀ ᴅᴏɴᴀᴛɪᴏɴs ᴄᴀɴ ᴀʟsᴏ ᴍᴏᴛɪᴠᴀᴛᴇ ᴜs ᴋᴇᴇᴘ ʙʀɪɴɢ ᴏɴ ɴᴇᴡ ғᴇᴀᴛᴜʀᴇs.

Yᴏᴜ ᴄᴀɴ ʜᴇʟᴘ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ ᴡɪᴛʜ ᴅᴏɴᴀᴛɪᴏɴs</b>"""

    ZOMBIES_TXT = """<b>ʜᴇʟᴩ ʏou ᴛᴏ ᴋɪᴄᴋ ᴜꜱᴇʀꜱ 

Kɪᴄᴋ ɪɴᴄᴀᴛɪᴠᴇ ᴍᴇᴍʙᴇʀꜱ ғʀᴏᴍ ɢʀᴏᴜᴘ. Aᴅᴅ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ᴡɪᴛʜ ʙᴀɴ ᴜꜱᴇʀꜱ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ɪɴ ɢʀᴏᴜᴘ.

Cᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ Uꜱᴀɢᴇ:

• /inkick - ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ʀᴇǫᴜɪʀᴇᴅ ᴀʀɢᴜᴍᴇɴᴛꜱ ᴀɴᴅ ɪ ᴡɪʟʟ ᴋɪᴄᴋ ᴍᴇᴍʙᴇʀꜱ ғʀᴏᴍ ɢʀᴏᴜᴘ.
• /instatus - ᴛᴏ ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ ᴏғ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀ ғʀᴏᴍ ɢʀᴏᴜᴘ.
• /inkick ᴡɪᴛʜɪɴ_ᴍᴏɴᴛʜ ʟᴏɴɢ_ᴛɪᴍᴇ_ᴀɢᴏ - ᴛᴏ ᴋɪᴄᴋ ᴜꜱᴇʀꜱ ᴡʜᴏ ᴀʀᴇ ᴏғғʟɪɴᴇ ғᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ 𝟼-𝟽 ᴅᴀʏꜱ.
• /inkick ʟᴏɴɢ_ᴛɪᴍᴇ_ᴀɢᴏ - ᴛᴏ ᴋɪᴄᴋ ᴍᴇᴍʙᴇʀꜱ ᴡʜᴏ ᴀʀᴇ ᴏғғʟɪɴᴇ ғᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ ᴀ ᴍᴏɴᴛʜ ᴀɴᴅ Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛꜱ.
• /dkick - ᴛᴏ ᴋɪᴄᴋ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ.</b>"""

    REPORT_MSG = """ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs"""

    REPORT_TXT = """@admins, @admins, /report. ғᴏʀ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs(ᴡᴏʀᴋ ᴏɴʟʏ ɪɴ  ɢʀᴏᴜᴘ)"""

    VSONG = """
» ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ sᴏɴɢ ᴀɴᴅ ᴠɪᴅᴇᴏ :

➻ /vsong - ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ʏᴏᴜᴛᴜʙᴇ sᴏɴɢ
➻ /vvideo - ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ
➻ /song - sᴘᴏᴛɪғʏ sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ
"""
    CHATAI = """
» ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ   ᴄʜᴀᴛ ᴀɪ :

 ᴀɪ ᴄᴀɴ ᴀɴsᴡᴇʀ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ  ᴀɴᴅ sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ ʀᴇsᴜʟᴛ

 /chatgpt  : ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ
 /lucy : ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ
 /ask : ᴀɪ ɢᴏᴏɢʟᴇ ᴀɪ 
 /gpt : chatgpt
 /chat :  ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ
"""
    ENCRYPT = """
» ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ ᴇɴᴄʀʏᴘᴛ :

ᴄᴏɴᴠᴇʀᴛs
 /encrypt: ᴇɴᴄʀʏᴘᴛs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
 /decrypt: ᴅᴇᴄʀʏᴘᴛs ᴘʀᴇᴠɪᴏᴜsʟʏ ᴇᴄʀʏᴘᴛᴇᴅ ᴛᴇxᴛ
 /encode: ᴇɴᴄᴏᴅᴇ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
 /decode: ᴅᴇᴄᴏᴅᴇ ᴘʀᴇᴠɪᴏᴜsʟʏ ᴇᴄʀʏᴘᴛᴇᴅ ᴛᴇxᴛ
 /morseencode: Mᴏʀsᴇ Eɴᴄᴏᴅᴇ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
 /morsedecode: ᴅᴇᴄʀʏᴘᴛs ᴘʀᴇᴠɪᴏᴜsʟʏ ᴇᴄʀʏᴘᴛᴇᴅ ᴛᴇxᴛ
 /password :  ɢɪᴠᴇ ʟᴇɴɢᴛʜ ᴏғ ᴘᴀssᴡᴏʀᴅ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ
 /uselessfact : Gᴇɴᴇʀᴀᴛᴇ  Rᴀᴍᴅᴏᴍ Usᴇʟᴇss Fᴀᴄᴛ
"""
    YTSEARCH = """
The YouTube search module is a feature on the YouTube platform that allows users to search for specific videos, channels, or topics. When you enter a search query in the search bar on YouTube, the search module displays relevant results based on your query. You can filter the results by videos, channels, playlists, or live streams to find the content you are looking for. The search module also provides suggestions as you type, making it easier to discover new content on YouTube. Additionally, the search module may display trending or popular videos related to your search query. Overall, the YouTube search module is a powerful tool that helps users find and explore a wide range of video content on the platform.

ᴄᴏᴍᴍᴀɴᴅ
 /ytsearch: sᴇᴀʀᴄʜ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ
 /google : google search
"""
    FIGLET_TXT = """
» ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ Fɪɢʟᴇᴛ :

/figlet: ᴍᴀᴋᴇs ғɪɢʟᴇᴛ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
Example:

/figlet icecube
"""

    WALL = """
» ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ ᴡᴀʟʟᴘᴀᴘᴇʀs:

/wall: sᴇᴀʀᴄʜ ᴡᴀʟʟᴘᴀᴘᴇʀ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
/wallpaper : sᴇᴀʀᴄʜ ᴡᴀʟʟᴘᴀᴘᴇʀ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
Example:

/wall icecube
"""
    GROUPDATA = """
ɢᴇᴛ ɢʀᴏᴜᴘ ɪɴғᴏʀᴍᴀᴛɪᴏɴ

 /groupdata 
 /groupinfo 

note: ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs
"""
    TAGALL = """
» ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ Tᴀɢ Aʟʟ :

Only for admins

/tagall or @all '(reply to message or add another message) To mention all members in your group, without exception.'
/tagoff : ᴄᴀɴᴄᴇʟ ᴀʟʟ ᴍᴇɴᴛɪᴏɴꜱ
/hitag : ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs
/lifetag : ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs
/histop or /lifestop : ᴄᴀɴᴄᴇʟ ᴀʟʟ ᴍᴇɴᴛɪᴏɴꜱ
"""

    BG_TXT = """
ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇʀ ᴛᴏᴏʟ:

Our background remover tool is a powerful and easy-to-use solution for removing backgrounds from images. With just a few clicks, you can quickly and accurately remove the background from any photo, leaving you with a clean and professional-looking image. Whether you're a photographer looking to enhance your images or a graphic designer working on a project, our background remover tool is the perfect solution for all your editing needs. Say goodbye to tedious manual editing and let our tool do the work for you, saving you time and effort. Try it today and see the difference it can make in your images!

ᴇxᴀᴍᴘʟᴇ : /rmbg ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ
"""

    TORRENT = """
ᴛᴏʀʀᴇɴᴛ sᴇᴀʀᴄʜ ᴄᴏᴍᴍᴀɴᴅ

ᴇxᴀᴍᴘʟᴇ : /torrent ᴍᴏɴᴇʏ ʜᴇɪsᴛ
"""

    RING_TXT = """
ʀɪɴɢᴛᴜɴᴇ ᴄᴏᴍᴍᴀɴᴅ

ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ʀɪɴɢᴛᴜɴᴇ ɪɴ ᴛʜᴇ ғʀᴏᴍ ᴏғ /ringtune {sᴏɴɢ_ɴᴀᴍᴇ + ᴀʀᴛɪsᴛ_ɴᴀᴍᴇ} ᴏʀ {sᴏɴɢ_ɴᴀᴍᴇ}
"""

    FUN_TXT = """
Make your chats funny with lot's Fun Module!

USAGE:
➢ /punch - Sends Random punch GIFs.
➢ /slap - Sends Random Slap GIFs.
➢ /lick - Sends Random Lick GIFs.
➢ /kill - Sends Random Kill GIFs.
➢ /kick - Sends Random Kick GIFs.
➢ /hug - Sends Random Hug GIFs.
➢ /dare - Play truth or dare.
➢ /truth - Play truth or dare.
➢ /bite - Sends Random Bite GIFs.
➢ /meme - Awesome memes everytime.
➢ /kiss - Sends Random Kiss GIFs.
➢ /waifu - get any random waifu
➢ /highfive - Sends Random Highfive GIFs.
"""

    MONGO_TXT = """
ᴍᴏɴɢᴏ ᴄʜᴇᴄᴋ ᴄᴏᴍᴍᴀɴᴅ

ᴇɴᴛᴇʀ ʏᴏᴜʀ MᴏɴɢᴏDB URL ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ.

exᴀᴍᴘʟᴇ: /mongo ʏᴏᴜʀ_ᴍᴏɴɢᴏᴅʙ_ᴜʀʟ
"""

    SPECIAL_MOD1 = """
» ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ Aɪ and ai ɪᴍᴀɢᴇ :

 ➻ /imagine : ɢᴇɴᴇʀᴀᴛᴇ Aɪ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛᴇxᴛ
 ➻ /mahadev : ɢᴇɴᴇʀᴀᴛᴇ Mᴀʜᴀᴅᴇᴠ ɪᴍᴀɢᴇ
 ➻ /upscale : ᴜᴘsᴄᴀʟᴇ ʏᴏᴜʀ ɪᴍᴀɢᴇs
 ➻ /gpt : ᴄʜᴀᴛɢᴘᴛ
 ➻ /draw : ᴄʀᴇᴀᴛᴇ ɪᴍᴀɢᴇs

ɴᴏᴛᴇ:
• MovieVerse sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ.

ᴘᴏᴡᴇʀᴇᴅ ʙʏ MovieVerse Bot...
"""

    SPECIAL_MOD2 = """
ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴛʜᴇ ғᴀᴋᴇ ɪɴғᴏ ᴍᴏᴅᴜʟᴇ:

USAGE:
➢ /fake : ɢᴇɴᴇʀᴀᴛᴇs ғᴀᴋᴇ Iɴғᴏʀᴍᴀᴛɪᴏɴ
➢ /picgen : Generate a Fake pic

ɴᴏᴛᴇ:
• MovieVerse sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ.

ᴘᴏᴡᴇʀᴇᴅ ʙʏ MovieVerse Bot...
"""

    EXTRA_MOD = """
ᴛʜᴇʀᴇ ᴀʀᴇ sᴏᴍᴇ ᴏғ ᴍɪɴᴇ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇs, ᴇɴɪᴏʏ!

➢ /imdb - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏ ғʀᴏᴍ IMDʙ.
➢ /eval - ᴛᴏ ᴇᴠᴀʟᴜᴀᴛᴇ sɪᴍᴘʟᴇ ᴄᴏᴅᴇ
➢ /info - ᴛᴏ get ur info
➢ /animememe - ɢᴇᴛ ᴀɴɪᴍᴇ ᴍᴇᴍᴇs.
➢ /write - ᴡʀɪᴛᴇ ᴛᴇxᴛ ᴀs ʜᴀɴᴅᴡʀɪᴛɪɴɢ.
➢ /afk - ᴍᴀʀᴋ ʏᴏᴜʀsᴇʟғ ᴀs ᴀғᴋ.
➢ /truth  : sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.
➢ /dare  : sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.
➢ /song : ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ
➢ /spotify : ғɪɴᴅ ᴛʜᴇ sᴏɴɢ ᴅᴇᴛᴀɪʟs ʙʏ ᴜʀ ʀᴇǫᴜᴇsᴛ
➢ /instagram : sᴇɴᴅ ɪɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟ,sᴛᴏʀɪᴇs ᴀɴᴅ ᴘᴏsᴛ ʟɪɴᴋ ᴛᴏ ᴛʜɪs ʙᴏᴛ, ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ, ᴘᴜʙʟɪᴄ ᴏɴʟʏ.
➢ /autorequst : ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ᴜʀ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ ᴀɴᴅ sᴇᴇ ᴍᴀɢɪᴄ
➢ /t2f - ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛʜᴇ ᴛᴇxᴛ ᴛᴏ ғɪʟᴇ ᴡɪᴛʜ ᴀɴʏ ᴛᴇxᴛ ғɪʟᴇ ғᴏʀᴍᴀᴛs
➢ /logo (Text) : ᴄʀᴇᴀᴛᴇ ᴀ ʟᴏɢᴏ ᴏғ ʏᴏᴜʀ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴡɪᴛʜ ʀᴀɴᴅᴏᴍ ᴠɪᴇᴡ.
➢ /animelogo (Text) : ᴄʀᴇᴀᴛᴇ ᴀ anime ʟᴏɢᴏ ᴏғ ʏᴏᴜʀ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴡɪᴛʜ ʀᴀɴᴅᴏᴍ ᴠɪᴇᴡ.

ɴᴏᴛᴇ:
• MovieVerse sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ.

ᴘᴏᴡᴇʀᴇᴅ ʙʏ MovieVerse Bot...
"""


    SPECIAL_TXT = """
ᴄʜᴇᴄᴋ ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴅᴜʟᴇ
"""

    EXPERT_TXT = """
ᴛʜᴇsᴇ ᴀʀᴇ sᴏᴍᴇ ᴀɪ/ᴇxᴘᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅs

 ➻ /mahadev : ɢᴇɴᴇʀᴀᴛᴇ Mᴀʜᴀᴅᴇᴠ ɪᴍᴀɢᴇ
 ➻ /fakegen : ɢᴇɴᴇʀᴀᴛᴇs ғᴀᴋᴇ Iɴғᴏʀᴍᴀᴛɪᴏɴ
 ➻ /picgen : ɢᴇɴᴇʀᴀᴛᴇ ᴀ ғᴀᴋᴇ ᴘɪᴄ
 ➻ /eval : ᴛᴏ ᴇᴠᴀʟᴜᴀᴛᴇ sɪᴍᴘʟᴇ ᴄᴏᴅᴇ
 ➻ /ask : ʀᴇᴘʟʏ ᴛo ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ
 ➻ /draw : ᴄʀᴇᴀᴛᴇ ɪᴍᴀɢᴇs
 ➻ /upscale : ᴜᴘsᴄᴀʟᴇ ʏᴏᴜʀ ɪᴍᴀɢᴇs
 ➻ /gpt : ᴄʜᴀᴛɢᴘᴛ
 ➻ /lucy : ᴀɪ ʙʏ ɢᴏᴏɢʟᴇ
 ➻ /reverse : ʀᴇᴠᴇʀsᴇ ɪᴍᴀɢᴇ sᴇᴀʀᴄʜ
 ➻ /imagine : ᴄʀᴇᴀᴛᴇ ᴀɪ ɪᴍᴀɢᴇs

ɴᴏᴛᴇ:
• MovieVerse sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ.

ᴘᴏᴡᴇʀᴇᴅ ʙʏ MovieVerse Bot..
"""

    SUPPORT_TXT = """ᴛʜᴇsᴇ ᴀʀᴇ ᴍʏ sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢʀᴏᴜᴘ. ɪғ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ʀᴇᴘᴏʀᴛ ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴ
ᴘᴏᴡᴇʀᴇᴅ ʙʏ - <b>[MovieVerse](https://t.me/movieversepremium)</b>"""
    
    STATUS_TXT = """<b>    
‣ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ MovieVerse :

• ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ : <code>{}</code>
• ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : <code>{}</code>
• ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘꜱ : <code>{}</code>
• ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ : <code>{}</code>
• ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ : <code>{}</code>
</b>"""

    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

◉ ɢʀᴏᴜᴩ: {}(<code>{}</code>)
◉ ᴍᴇᴍʙᴇʀꜱ: {}
◉ ᴀᴅᴅᴇᴅ ʙʏ: {}"""

    LOG_TEXT_P = """#ɴᴇᴡ_ᴜꜱᴇʀ
    
◉ ᴜꜱᴇʀ-ɪᴅ: <code>{}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {}"""

    ALRT_TXT = """{},
ᴄʜᴇᴄᴋ  ʏᴏᴜʀ  ᴏᴡɴ  ʀᴇǫᴜᴇ𝗌ᴛ
"""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɴᴏᴛ ғᴏᴜɴᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ.**\n\n» ᴍᴀʏʙᴇ ᴛᴜɴᴇ ɢᴀʟᴀᴛ ʟɪᴋʜᴀ ʜᴏ, ᴩᴀᴅʜᴀɪ - ʟɪᴋʜᴀɪ ᴛᴏʜ ᴋᴀʀᴛᴀ ɴᴀʜɪ ᴛᴜ !"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 

ᴍᴏᴠɪᴇ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ʀᴇᴀsᴏɴ :

1) ᴏ.ᴛ.ᴛ ᴏʀ ᴅᴠᴅ ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ

2) ᴛʏᴘᴇ ɴᴀᴍᴇ ᴡɪᴛʜ ʏᴇᴀʀ

3) ᴍᴏᴠɪᴇ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs</b>"""

    I_CUD_NT = """<b>ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.

ᴍᴏᴠɪᴇ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ʀᴇᴀsᴏɴ :

1) ᴏ.ᴛ.ᴛ ᴏʀ ᴅᴠᴅ ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ

2) ᴛʏᴘᴇ ɴᴀᴍᴇ ᴡɪᴛʜ ʏᴇᴀʀ

3) ᴍᴏᴠɪᴇ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs</b>"""

    MVE_NT_FND = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ

ᴍᴏᴠɪᴇ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ʀᴇᴀsᴏɴ :

1) ᴏ.ᴛ.ᴛ ᴏʀ ᴅᴠᴅ ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ

2) ᴛʏᴘᴇ ɴᴀᴍᴇ ᴡɪᴛʜ ʏᴇᴀʀ

3) ᴍᴏᴠɪᴇ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs</b>"""
    

    TOP_ALRT_MSG = """Searching For Query In My Database..."""

    MELCOW_ENG = """<b>›› ʜᴇʏ {}, ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {} \n\nʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ꜱᴇᴀʀᴄʜ ʏᴏᴜʀ ꜰᴀᴠᴏᴜʀɪᴛᴇ ᴍᴏᴠɪᴇꜱ ᴏʀ ꜱᴇʀɪᴇꜱ ʙʏ ᴊᴜꜱᴛ ᴛʏᴘɪɴɢ ɪᴛ'ꜱ ɴᴀᴍᴇ\n\n›› ɪꜰ ʏᴏᴜ'ʀᴇ ʜᴀᴠɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʀᴇɢᴀʀᴅɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴏʀ ꜱᴏᴍᴇᴛʜɪɴɢ ᴇʟꜱᴇ ᴛʜᴇɴ ᴍᴇꜱꜱᴀɢᴇ ʜᴇʀᴇ</b>"""

    DISCLAIMER_TXT =  """<b>ᴛʜɪꜱ ɪꜱ not ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪᴅᴅᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.

ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/MovieVerse_2_bot">IceCube</a></b>"""

    USERS_TXT = """ʜᴇʏ {},

ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴜꜱᴇʀꜱ ⇊
    
• /batch - ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.
• /link - ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.
• /pbatch - ᴊᴜsᴛ ʟɪᴋᴇ <code>/batch</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
• /plink - ᴊᴜsᴛ ʟɪᴋᴇ <code>/link</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.
• /id - ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.
• /info  - ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.
• /imdb  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.
• /search  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ.
• /stats - ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ.
• /request - sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. ( ᴏɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ )
• /plan - ᴄʜᴇᴄᴋ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ ᴘʟᴀɴꜱ.
• /myplan - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴜɴᴛ ᴘʟᴀɴ."""

    GROUP_TXT = """ʜᴇʏ {},

ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀꜱ ⇊
    
• /connect  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ.
• /disconnect  - ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.
• /set_shortlink - ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ꜱʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ.
• /remove_tutorial - ꜱᴇᴛ ʏᴏᴜʀ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ.
• /shortlink_info - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ.
• /setshortlinkon - ᴏɴ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
• /setshortlinkoff - ᴏꜰꜰ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
• /connections - ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ.
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ.
• /filter - ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /filters - ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ɢʀᴏᴜᴘ.
• /del - ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ɢʀᴏᴜᴘ.
• /purge - ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇssᴀɢᴇ."""

    ADMINS_TXT = """ʜᴇʏ {},

ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴀᴅᴍɪɴꜱ ⇊
    
• /logs - <code>ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ.</code>
• /delete - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /leave  - <code>ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘꜱ.</code>
• /broadcast - <code>ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.</code>
• /grp_broadcast - <code>ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /gfilters - <code>ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /send - <code>ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.</code>
• /gsend -  <code>send message to any group</code>
• /add_premium - <code>ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.</code>
• /remove_premium - <code>ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.</code>
• /premium_users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.</code>
• /get_premium - <code>ɢᴇᴛ ɪɴꜰᴏ ᴏꜰ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ.</code>
• /restart - <code>ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.</code>"""

    MANAGEMENT_TXT = """
👮🏻aᴠᴀɪʟᴀʙʟᴇ ᴛᴏ aᴅᴍɪɴs & mᴏᴅᴇʀᴀᴛᴏʀs.

🕵🏻 /settings ʟᴇᴛs ʏᴏᴜ ᴍᴀɴᴀɢᴇ ᴀʟʟ ᴛʜᴇ Bᴏᴛ sᴇᴛᴛɪɴɢs ɪɴ ᴀ ɢʀᴏᴜᴘ.
 /ban ʙᴀɴ ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.
 /mute ᴘᴜᴛs ᴀ ᴜsᴇʀ ɪɴ ʀᴇᴀᴅ-ᴏɴʟʏ ᴍᴏᴅᴇ. Hᴇ ᴄᴀɴ ʀᴇᴀᴅ ʙᴜᴛ ʜᴇ ᴄᴀɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇs.
 /kick kick ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ.
 /unban ʟᴇᴛs ʏᴏᴜ ʀᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ ɢʀᴏᴜᴘ's ʙʟᴀᴄᴋʟɪsᴛ
 /report - ᴛᴏ ʀᴇᴘʟʏ ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ғᴏʀ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs [ғᴏʀ ᴜsᴇʀs]
 /fp - ᴛᴏ sᴇɴᴅ ʏᴏᴜʀ ғᴇᴇᴅʙᴀᴄᴋ ʙʏ ᴘᴜʙʟɪᴄᴀʟʟʏ [ғᴏʀ ᴜsᴇʀs]
 /connect - ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ʙᴏᴛ
 /filter - ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ.
 /filters - ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ɢʀᴏᴜᴘ.
 /del - ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ.
 /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ɢʀᴏᴜᴘ.
 /purge - ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ꜰʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇssᴀɢᴇ.
 /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)
 /promote - promote any user to admin
 /demote - demote any user.

ɴᴏᴛᴇ:
• MovieVerse sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ.

ᴘᴏᴡᴇʀᴇᴅ ʙʏ MovieVerse Bot..
"""

    SHORTLINK_INFO = """
 <b> <u>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ᴜꜱɪɴɢ ʙᴏᴛ</u>

★ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ꜱᴛᴀʀᴛ ᴇᴀʀɴɪɴɢ ᴍᴏɴᴇʏ ᴛᴏᴅᴀʏ ᴡɪᴛʜ ᴏᴜʀ ꜱɪᴍᴘʟᴇ ᴀɴᴅ ᴇᴀꜱʏ-ᴛᴏ-ᴜꜱᴇ ʙᴏᴛ!

›› ꜱᴛᴇᴘ 1 : ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀꜱ ᴀɴ ᴀᴅᴍɪɴ...

›› ꜱᴛᴇᴘ 2 : ᴜꜱᴇ /connect ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ.

›› ꜱᴛᴇᴘ 3 : ᴄʟɪᴄᴋ ᴏɴ ɴᴇxᴛ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ꜱʜᴏʀᴛʟɪɴᴋ ᴡᴇʙꜱɪᴛᴇ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

★ ᴅᴏɴ'ᴛ ᴡᴀɪᴛ ᴀɴʏ ʟᴏɴɢᴇʀ ᴛᴏ ꜱᴛᴀʀᴛ ᴇᴀʀɴɪɴɢ ᴍᴏɴᴇʏ ꜰʀᴏᴍ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ. ᴀᴅᴅ ᴏᴜʀ ʙᴏᴛ ᴛᴏᴅᴀʏ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴍᴀᴋɪɴɢ ᴍᴏɴᴇʏ!</b>
"""

    SHORTLINK_INFO2 = """<b>
<u>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ</u>

›› ꜱᴛᴇᴘ 4 : ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴜꜱɪɴɢ ᴀɴʏ ꜱʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ ᴛʜᴇɴ ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ꜰɪʀꜱᴛ ᴏɴ viplinkshortx.in (ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴜꜱᴇ ᴏᴛʜᴇʀ ʟɪɴᴋ ꜱʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ).

›› ꜱᴛᴇᴘ 5 : ᴄᴏᴘʏ ʏᴏᴜʀ ᴀᴘɪ ꜰʀᴏᴍ ᴡᴇʙꜱɪᴛᴇ ᴀɴᴅ ᴛʜᴇɴ, ꜱɪᴍᴘʟʏ ꜱᴇᴛ ʏᴏᴜʀ ᴡᴇʙꜱɪᴛᴇ ᴀɴᴅ ᴀᴘɪ ᴜꜱɪɴɢ ᴛʜᴇ /set_shortlink ᴄᴏᴍᴍᴀɴᴅ.

› ʟɪᴋᴇ ᴛʜɪꜱ :</b>  <code>/set_shortlink viplinkshortx.in ae94aa02950078a27e61d002add8ca0ea8843e5a</code>

<b>›› ꜱᴛᴇᴘ 6 : ᴄʟɪᴄᴋ ᴏɴ ɴᴇxᴛ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴛᴜᴛᴏʀɪᴀʟ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

★ ᴛʜɪꜱ ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴄᴏɴᴠᴇʀᴛꜱ ʟɪɴᴋꜱ ᴡɪᴛʜ ʏᴏᴜʀ ᴀᴘɪ ᴀɴᴅ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ.</b>
"""
    SHORTLINK_INFO3 = """<b>
<u>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴛᴜᴛᴏʀɪᴀʟ</u>

›› ꜱᴛᴇᴘ 7 : ᴜꜱᴇ /set_tutorial ᴛᴏ ᴀᴅᴅ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ꜰᴏʀ ʏᴏᴜʀ ꜱʜᴏʀᴛɴᴇʀ ᴡᴇʙꜱɪᴛᴇ.

› ʟɪᴋᴇ ᴛʜɪꜱ :</b> <code>/set_tutorial https://t.me/howtoverify_97/3</code>

<b>›› ꜱᴛᴇᴘ 8 : ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ /shortlink_info ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

★ ᴛʜᴀᴛ'ꜱ ɪᴛ, ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴇᴀʀɴ ᴀ ʟᴏᴛ ᴍᴏɴᴇʏ ᴜꜱɪɴɢ ᴛʜɪs ʙᴏᴛ.</b>
"""
    
    SELECT = """
➢ ᴄʟɪᴄᴋ ᴏɴ "ǫᴜᴀʟɪᴛʏ" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ꜰɪʟᴇ ɪɴ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ǫᴜᴀʟɪᴛʏ.
➢ ᴄʟɪᴄᴋ ᴏɴ "ʟᴀɴɢᴜᴀɢᴇ" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ꜰɪʟᴇ ɪɴ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.
➢ ᴄʟɪᴄᴋ ᴏɴ "ꜱᴇᴀꜱᴏɴ" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ꜰɪʟᴇ ɪɴ ʏᴏᴜʀ ᴅᴇꜱɪʀᴇᴅ ꜱᴇᴀꜱᴏɴ.

➢ ᴄʟɪᴄᴋ ᴏɴ "ꜱᴇɴᴅ ᴀʟʟ ꜰɪʟᴇꜱ" ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ᴄʟɪᴄᴋ.

✯ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ʜᴘ
"""

    REQINFO = """➢ ᴄʟɪᴄᴋ "ǫᴜᴀʟɪᴛʏ" ᴀɴᴅ ᴄʜᴀɴɢᴇ ǫᴜᴀʟɪᴛʏ.
➢ ᴄʟɪᴄᴋ "ʟᴀɴɢᴜᴀɢᴇ" ᴀɴᴅ ᴄʜᴀɴɢᴇ ʟᴀɴɢᴜᴀɢᴇ.
➢ ᴄʟɪᴄᴋ "ꜱᴇᴀꜱᴏɴ" ᴀɴᴅ ᴄʜᴀɴɢᴇ ꜱᴇᴀꜱᴏɴ.
➢ ᴄʟɪᴄᴋ "ꜱᴇɴᴅ ᴀʟʟ ꜰɪʟᴇꜱ" ᴀɴᴅ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ."""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """ 
#NoResults

Iᴅ : <code>{}</code>
Nᴀᴍᴇ : {}

Mᴇꜱꜱᴀɢᴇ : <b>{}</b>"""
 
   # PLEASE DO NOT REMOVE ANY CREDITS ❤️‍🩹
    
    CAPTION = """<b>Fɪʟᴇɴᴀᴍᴇ : {file_name}

<b> Size: {file_size}</b>""" 

    IMDB_TEMPLATE_TXT = """
<b>Title: {title}</b>

<b>Genres:</b> {genres}
<b>Rating:</b> {rating}/10 Based on {votes} user ratings.
<b>RunTime:</b> {runtime} Minutes
<b>Release Info:</b> {release_date}


<b>Requested by: {message.from_user.mention}</b>

<b>Join Us: [MovieVerse Backup](https://t.me/movieversepremium)</b>"""
    
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

Dᴀᴛᴇ : <code>{}</code>
Tɪᴍᴇ : <code>{}</code>
Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>ᴠ4.4 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """
                _       __ _ _        _           _       
   ___ ___   __| | ___ / _| (_)_  __ | |__   ___ | |_ ___ 
  / __/ _ \ / _` |/ _ \ |_| | \ \/ / | '_ \ / _ \| __/ __|
 | (__ (_) | (_| |  __/  _| | |>  <  | |_) | (_) | |_\__ \
  \___\___/ \__,_|\___|_| |_|_/_/\_\ |_.__/ \___/ \__|___/

"""

    PAGE_TXT = """ᴡʜʏ ᴀʀᴇ ʏᴏᴜ ꜱᴏ ᴄᴜʀɪᴏᴜꜱ ⁉️"""

    PURCHASE_TXT = """ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ."""

    PREMIUM_TEXT = """<b>ʜᴇʏ {},
    
<u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u>

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>20₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>15 ᴅᴀʏꜱ</code>
● <code>30₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>40₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>45 ᴅᴀʏꜱ</code>
● <code>50₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>60 ᴅᴀʏꜱ</code>

ᴜᴘɪ ɪᴅ - <code>dm - @icecube9680</code>
ǫʀ ᴄᴏᴅᴇ - <a href='https://graph.org/file/e2d9b5e15e15daafb64e8.jpg'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    CPREMIUM_TEXT = """<b>ʜᴇʏ {},
    
<u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u>

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>20₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>15 ᴅᴀʏꜱ</code>
● <code>30₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>40₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>45 ᴅᴀʏꜱ</code>
● <code>50₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>60 ᴅᴀʏꜱ</code>

ᴜᴘɪ ɪᴅ - <code>dm - @icecube9680</code>
ǫʀ ᴄᴏᴅᴇ - <a href='https://graph.org/file/e2d9b5e15e15daafb64e8.jpg'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    PLAN_TXT = """<b>ʜᴇʏ {},
    
<u>ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs</u> :

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs                                                                        
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""

    FREE_TXT = """<b>ʜᴇʏ {},
    
<u>ꜰʀᴇᴇ ᴛʀɪᴀʟ</u>
 ᴏɴʟʏ ꜰᴏʀ 5 ᴍɪɴᴜᴛᴇꜱ
 
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ

ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ <a href='https://t.me/icecube9680_bot'>ᴏᴡɴᴇʀ</a> ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴛʀɪᴀʟ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    BRONZE_TXT = """<b>ʜᴇʏ {},
    
<u>ʙʀᴏɴᴄᴇ ᴘʟᴀɴ</u>
7 ᴅᴀʏꜱ
ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 10₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    SILVER_TXT = """<b>ʜᴇʏ {},
    
<u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u>
15 ᴅᴀʏꜱ 
ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 20₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    GOLD_TXT = """<b>ʜᴇʏ {},
    
<u>ɢᴏʟᴅ ᴘʟᴀɴ</u>
30 ᴅᴀʏꜱ 
ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 30₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    PLATINUM_TXT = """<b>ʜᴇʏ {},
    
<u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u>
45 ᴅᴀʏꜱ 
ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 40₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""
    
    DIAMOND_TXT = """<b>ʜᴇʏ {},

<u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u>
60 ᴅᴀʏꜱ 
ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 50₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    OTHER_TXT = """<b>ʜᴇʏ {},
    
<u>ᴏᴛʜᴇʀ ᴘʟᴀɴ</u>
ᴄᴜꜱᴛᴏᴍɪꜱᴇᴅ ᴅᴀʏꜱ
ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀʏꜱ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ᴘʟᴀɴ ᴀᴘᴀʀᴛ ꜰʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ᴘʟᴀɴ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀʟᴋ ᴛᴏ ᴏᴜʀ <a href='https://t.me/icecube9680_bot'>ᴏᴡɴᴇʀ</a> ᴅɪʀᴇᴄᴛʟʏ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.
    
ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴏᴛʜᴇʀ ᴘʟᴀɴ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    UPI_TXT = """<b>ʜᴇʏ {},
    
ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

ᴜᴘɪ ɪᴅ - <code>dm - @icecube9680</code>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    QR_TXT = """<b>ʜᴇʏ {},
    
ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

ǫʀ ᴄᴏᴅᴇ - <a href='https://graph.org/file/e2d9b5e15e15daafb64e8.jpg'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    PREPLANS_TXT = """<b>ʜᴇʏ {},
    
<u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u>

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>20₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>15 ᴅᴀʏꜱ</code>
● <code>30₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>40₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>45 ᴅᴀʏꜱ</code>
● <code>50₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>60 ᴅᴀʏꜱ</code>

ᴜᴘɪ ɪᴅ - <code>dm - @icecube9680</code>
ǫʀ ᴄᴏᴅᴇ - <a href='https://graph.org/file/e2d9b5e15e15daafb64e8.jpg'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""    

    DEVELOPER_TXT = """
special Thanks To ❤️ Developer -

-Owner [Owner of this bot ]<a href='https://t.me/icecube9680_bot'>IceCube</a>
"""

#- ᴄʀᴇᴅɪᴛ - Github - @Codeflix-bots , @erotixe
#- ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
#- ᴛʜᴀɴᴋ ʏᴏᴜ MovieVerse Bot ғᴏʀ ʜᴇʟᴘɪɴɢ ᴜs ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ 
#- ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ɢɪᴠɪɴɢ ᴍᴇ ᴄʀᴇᴅɪᴛ @Codeflix-bots  
#- ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ -> ᴛᴇʟᴇɢʀᴀᴍ @movieVerse_2_bot Community @Otakflix_Network </b>

