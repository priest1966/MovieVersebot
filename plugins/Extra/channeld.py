from pyrogram import filters
from pyrogram import Client, enums
from pyrogram.file_id import FileId
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.private & filters.forwarded)
async def info(motech, msg):
    if msg.forward_from:
        text = "<u>Forward Information 👀</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>Bot Info</u>"
        else:
            text += "<u>User Info</u>"
        text += f'\n\nName : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:

            text += f'\n\nUserName : @{msg.forward_from["username"]} \n\nID : <code>{msg.forward_from["id"]}</code>\n\nDC : {msg.forward_from["dc_id"]}'           
        else:
            text += f'\n\nID : `{msg.forward_from["id"]}`\n\n\n\nDC : {msg.forward_from["dc_id"]}'

        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"️Error <b><i>{hidden}</i></b> ️Error",
                quote=True,
            )
        else:
            text = f"<u>Forward Information</u>.\n\n"
            if msg.forward_from_chat["type"] == enums.ChatType.CHANNEL:
                text += "<u>Channel</u>"
            if msg.forward_from_chat["type"] == enums.ChatType.GROUP:
                text += "<u>Group</u>"
            text += f'\n\nName {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:

                text += f'\n\nFrom : @{msg.forward_from_chat["username"]}'
                text += f'\n\nID : `{msg.forward_from_chat["id"]}`\n\nDC : {msg.forward_from_chat["dc_id"]}'
            else:
                text += f'\n\nID `{msg.forward_from_chat["id"]}`\n\n{msg.forward_from_chat["dc_id"]}'                                           

            await msg.reply(text, quote=True)
