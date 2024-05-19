from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import asyncio
from Bot import app 

START_TEXT = (
    "Hey {first_name}, ⚡️\n"
    "๏ ᴛʜɪs ɪs Shiva, !\n"
    "➻ Shiva is an Anime themed group management bot with some fun extras.\n"
    "──────────────────\n"
    "๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ Command ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs."
)

G_MSG = "Hello {first_name}, start the bot in pm"

HELP_TEXT = (
    "Shiva commands available:\n"
    "➛ /help: PM's you this message.\n"
    "➛ /help <module name>: PM's you info about that module.\n"
    "➛ /donate: information on how to donate!\n"
    "➛ /settings:\n"
    "➛ in PM: will send you your settings for all supported modules.\n"
    "➛ in a group: will redirect you to pm, with all that chat's settings."
)

BUTTON = [
    [InlineKeyboardButton("🔙 Back", callback_data="help_back"),
     InlineKeyboardButton("🗑 Close", callback_data='close')]
]

HELP_BUTTON = [
    [InlineKeyboardButton('👮 Admin', callback_data='admin_help'),
     InlineKeyboardButton('👥 UserInfo', callback_data='userinfo_help'),
     InlineKeyboardButton('🤗 Fun', callback_data='fun_help')],
    [InlineKeyboardButton('👻 Misc', callback_data='misc_help'),
     InlineKeyboardButton('🔍 Tagging', callback_data='tagging_help'),
     InlineKeyboardButton('✍ Notes', callback_data='notes_help')],
    [InlineKeyboardButton('🧚 Nekos', callback_data='nekos_help'),
     InlineKeyboardButton('❌ Ban-All', callback_data='banall_help'),
     InlineKeyboardButton('🤖 Ai', callback_data='ai_help')],
    [InlineKeyboardButton('☠ Zombies', callback_data='zombies_help'),
     InlineKeyboardButton('✏ Rename', callback_data='rename_help'),
     InlineKeyboardButton('📩 Paste', callback_data='paste_help')],
    [InlineKeyboardButton('🏡 Home', callback_data='home')]
]

ADMIN_TEXT = (
    "Usage of Admin commands:\n"
    "• /admins - to find group admins.\n"
    "• /promote - promote a user.\n"
    "• /demote - demote a user.\n"
    "• /kick - kick a user.\n"
    "• /ban - ban a user.\n"
    "• /unban - unban a user.\n"
    "• /pin - pin a message.\n"
    "• /unpin - unpin a message.\n"
    "• /del - delete a message.\n"
    "• /setgpic - set group pic.\n"
    "• /setgtitle - set group title.\n"
    "• /purge - purge a message."
)

USERINFO_TEXT = (
    "User Info:\n"
    "• /id - userid & chatid.\n"
    "• /info - user information."
)

MISC_TEXT = (
    "Extra commands:\n"
    "• /tm - reply media to get telegraph link.\n"
    "• /txt - reply text with suitable name and get telegraph text link.\n"
    "• /tr - reply text to translate the message.\n"
    "• /gen - to generate image.\n"
    "• /git - sent github username to view profile.\n"
    "• /ud - sent word for search urban dictionary.\n"
    "• /q - reply message to quotly.\n"
    "• /write - to write a message."
)

TAGGING_TEXT = (
    "Tagging a group members:\n"
    "• /tagall - tag a group members.\n"
    "• /stop - stop tagging."
)

FUN_TEXT = (
    "Usage of Fun commands:\n"
    "• /react - react a message.\n"
    "• /aq - random sent animequotes.\n"
    "• /dice - sent a dice.\n"
    "• /truth - sent a truth message.\n"
    "• /dare - sent a dare message."
)


@app.on_message(filters.command("start") & filters.group)
async def start(client, message):
    PM = [[
        InlineKeyboardButton("Click here", url="http://T.me/ShivaXtestProbot?start=true")
    ]]
    await message.reply_photo(
        photo="https://telegra.ph/file/40b478d7e9c0a7df55881.jpg",
        caption=G_MSG.format(first_name=message.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(PM)
    )
    await message.delete()

@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    
    await message.reply_photo(
        photo="http://telegra.ph/file/cc3c8743925134dad8f1a.jpg",
        caption=f"Hello {message.from_user.first_name}! <code> Starting the bot</code>"
    )
    await asyncio.sleep(0.9)
    reply1 = await message.reply_text('<code> Starting </code>')
    await asyncio.sleep(0.9)
    reply2 = await reply1.edit('<code> Starting .  </code>')
    await asyncio.sleep(0.9)
    reply3 = await reply2.edit('<code> Starting . .  </code>')
    await asyncio.sleep(0.9)
    reply4 = await reply3.edit('<code> Starting . . .  </code>')
    await asyncio.sleep(0.9)
    await reply4.delete()
    await asyncio.sleep(0.9)

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨Add me To Your Group✨", url="https://telegram.dog/ddmon_test_Bot?startgroup=true")
            ],
            [
                InlineKeyboardButton("⚡️Commands⚡️", callback_data="com"),
                InlineKeyboardButton("⭐️Support⭐️", url="https://t.me/Shivasupport_chat")
            ],
            [
                InlineKeyboardButton("🎵Music🎵", callback_data="mus")
            ]
        ]
    )

    await message.reply_photo(
        photo="https://telegra.ph/file/40b478d7e9c0a7df55881.jpg",
        caption=START_TEXT.format(first_name=message.from_user.first_name),
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex("^com$"))
async def commands(_, callback_query):
    await callback_query.answer()
    await callback_query.message.reply_text(
        HELP_TEXT,
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )


@app.on_message(filters.command("help"))
async def help_command(_, message):
    if message.chat.type == "private":
        await message.reply_text(
            HELP_TEXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )


@app.on_callback_query(filters.regex("help_back"))
async def help_back(_, query):
    await query.message.edit_text(
        HELP_TEXT, 
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )


@app.on_callback_query(filters.regex("close"))
async def close(_, query):
    await query.message.delete()


@app.on_callback_query(filters.regex("admin_help"))
async def admin_help(_, query):
    await query.message.edit_text(
        ADMIN_TEXT, 
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )


@app.on_callback_query(filters.regex("userinfo_help"))
async def userinfo_help(_, query):
    await query.message.edit_text(
        USERINFO_TEXT, 
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )


@app.on_callback_query(filters.regex("misc_help"))
async def misc_help(_, query):
    await query.message.edit_text(
        MISC_TEXT, 
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )


@app.on_callback_query(filters.regex("tagging_help"))
async def tagging_help(_, query):
    await query.message.edit_text(
        TAGGING_TEXT, 
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )


@app.on_callback_query(filters.regex("fun_help"))
async def fun_help(_, query):
    await query.message.edit_text(
        FUN_TEXT, 
        reply_markup=InlineKeyboardMarkup(BUTTON)
    )
