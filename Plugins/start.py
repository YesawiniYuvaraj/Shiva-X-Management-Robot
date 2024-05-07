from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot import app 

@app.on_message(filters.command("start") & filters.private)
async def start(client, message, query):
    await query.message.reply_text("⚡️")
    await query.message.edit_text("⚡️")
    await query.message.edit_text("✋")

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Command", callback_data="com")]]
    )

    await query.message.reply_text(
        f"Hey {message.from_user.first_name}, 🥀\n"
        "๏ ᴛʜɪs ɪs Shiva, !\n"
        "➻ Shiva ɪs ᴀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ sᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴘʟᴜɢɪɴs.\n"
        "──────────────────\n"
        "๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.",
        reply_markup=keyboard
  )
