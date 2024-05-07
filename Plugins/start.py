from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot import app 

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("⚡️")

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Command", callback_data="com")]]
    )

    await message.reply_photo(
        photo="https://telegra.ph/file/40b478d7e9c0a7df55881.jpg",
        caption=f"Hey {message.from_user.first_name}, 🥀\n"
                "๏ ᴛʜɪs ɪs Shiva, !\n"
                "➻ Shiva ɪs ᴀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ sᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴘʟᴜɢɪɴs.\n"
                "──────────────────\n"
                "๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.",
        reply_markup=keyboard
    )
