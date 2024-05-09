from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot import app 

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("👾")

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨Add me To Your Group✨", url="https://telegram.dog/ddmon_test_Bot?startgroup=true")
            ],
            [
                InlineKeyboardButton("⚡️Commands⚡️", callback_data="com"),
                InlineKeyboardButton("⭐️Support⭐️", url="https://t.me/ShivaSupportChat")
            ],
            [
                InlineKeyboardButton("🎵Music", callback_data="mus")
            ]
        ]
    )

    await message.reply_photo(
        photo="https://telegra.ph/file/40b478d7e9c0a7df55881.jpg",
        caption=f"Hey {message.from_user.first_name}, ⚡️\n"
        "๏ ᴛʜɪs ɪs Shiva, !\n"
        "➻ Shiva is an is an Anime themed group management bot with some fun extras.\n"
        "──────────────────\n"
        "๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ Command ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.",
        reply_markup=keyboard
    )
