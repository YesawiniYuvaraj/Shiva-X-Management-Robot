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
                InlineKeyboardButton("🎵Music🎵", callback_data="mus")
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

@app.on_callback_query(filters.regex("^com$"))
async def commands(client, callback_query):
    await callback_query.answer()
    
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Open Commands Here", callback_data="HELP_BUTTON")]
        ]
    )

    text = (
        "Shiva commands available:\n"
        "➛ /help: PM's you this message.\n"
        "➛ /help <module name>: PM's you info about that module.\n"
        "➛ /donate: information on how to donate!\n"
        "➛ /settings:\n"
        "   ➛ in PM: will send you your settings for all supported modules.\n"
        "   ➛ in a group: will redirect you to pm, with all that chat's settings."
    )
    
    await callback_query.message.edit_text(text, reply_markup=keyboard)

HELP_BUTTON = [[
        InlineKeyboardButton('👮 Admin', callback_data='admin_help'),
        InlineKeyboardButton('👥 UserInfo', callback_data='userinfo_help'),
        InlineKeyboardButton('🤗 Fun', callback_data='fun_help'),
        ],[
        InlineKeyboardButton('👻 Misc', callback_data='misc_help'),
        InlineKeyboardButton('🔍 Tagging', callback_data='tagging_help'),
        InlineKeyboardButton('✍ Notes', callback_data='notes_help'),
        ],[
        InlineKeyboardButton('🧚 Nekos', callback_data='nekos_help'),
        InlineKeyboardButton('❌ Ban-All', callback_data='banall_help'),
        InlineKeyboardButton('🤖 Ai', callback_data='ai_help'),
        ],[
        InlineKeyboardButton('☠ Zombies', callback_data='zombies_help'),
        InlineKeyboardButton('✏ Rename', callback_data='rename_help'),
        InlineKeyboardButton('📩 Paste', callback_data='paste_help'),
        ],[
        InlineKeyboardButton('🏡 Home', callback_data='home')]]

@bot.on_callback_query(filters.regex("home"))
async def help(_, query: CallbackQuery):
    await query.message.edit_caption(START_TEXT,
                                    reply_markup=InlineKeyboardMarkup(buttons),)

@bot.on_callback_query(filters.regex("help_back"))
async def help(_, query: CallbackQuery):
    await query.message.edit_caption(HELP_TEXT,
                                    reply_markup=InlineKeyboardMarkup(HELP_BUTTON),)

@bot.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
           query = query.message
           await query.delete()

BUTTON = [[InlineKeyboardButton("🔙 Back", callback_data="help_back"),
            InlineKeyboardButton("🗑 Close", callback_data='close'),]]

ADMIN_TEXT = """
Usage of Admin commands:
• /admins - to find group admins.
• /promote - promote a user.
• /demote - demote a user.
• /kick - kick a user.
• /ban - ban a user.
• /unban - unban a user.
• /pin - pin a message.
• /unpin - unpin a message.
• /del - delete a message.
• /setgpic - set group pic.
• /setgtitle - set group title.
• /purge - purge a message.
"""

@bot.on_callback_query(filters.regex("admin_help"))
async def adminhelp(_, query: CallbackQuery):
     await query.message.edit_caption(ADMIN_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

USERINFO_TEXT = """
User Info:
• /id - userid & chatid.
• /info - user information.
"""

@bot.on_callback_query(filters.regex("userinfo_help"))
async def userinfohelp(_, query: CallbackQuery):
     await query.message.edit_caption(USERINFO_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
MISC_TEXT = """
Extra commands:
• /tm - reply media to get telegraph link.
• /txt - reply text with suitable name and get telegraph text link.
• /tr - reply text to translate the message.
• /gen - to generate image.
• /git - sent github username to view profile.
• /ud - sent word for search urban dictionary.
• /q - reply message to quotly.
• /write - to write a message.
"""

@bot.on_callback_query(filters.regex("misc_help"))
async def micshelp(_, query: CallbackQuery):
     await query.message.edit_caption(MISC_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
TAGGING_TEXT = """
Tagging a group members:
• /tagall - tag a group members.
• /stop - stop tagging.
"""

@bot.on_callback_query(filters.regex("tagging_help"))
async def tagginghelp(_, query: CallbackQuery):
     await query.message.edit_caption(TAGGING_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
FUN_TEXT = """
Usage of Fun commands:
• /react - react a message.
• /aq - random sent animequotes.
• /dice - sent a dice.
• /truth - sent a truth message.
• /dare - sent a dare message.
"""

@bot.on_callback_query(filters.regex("fun_help"))
async def funhelp(_, query: CallbackQuery):
     await query.message.edit_caption(FUN_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
