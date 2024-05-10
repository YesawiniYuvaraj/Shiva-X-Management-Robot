from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot import app 

START_TEXT = (
    "Hey {first_name}, ⚡️\n"
    "๏ ᴛʜɪs ɪs Shiva, !\n"
    "➻ Shiva is an is an Anime themed group management bot with some fun extras.\n"
    "──────────────────\n"
    "๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ Command ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs."
)

HELP_TEXT = "Shiva commands available:\n➛ /help: PM's you this message.\n➛ /help <module name>: PM's you info about that module.\n➛ /donate: information on how to donate!\n➛ /settings:\n➛ in PM: will send you your settings for all supported modules.\n➛ in a group: will redirect you to pm, with all that chat's settings."

BUTTON = [
    [
        InlineKeyboardButton("🔙 Back", callback_data="help_back"),
        InlineKeyboardButton("🗑 Close", callback_data="close")
    ]
]

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

USERINFO_TEXT = """
User Info:
• /id - userid & chatid.
• /info - user information.
"""

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

TAGGING_TEXT = """
Tagging a group members:
• /tagall - tag a group members.
• /stop - stop tagging.
"""

FUN_TEXT = """
Usage of Fun commands:
• /react - react a message.
• /aq - random sent animequotes.
• /dice - sent a dice.
• /truth - sent a truth message.
• /dare - sent a dare message.
"""

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
        caption=START_TEXT.format(first_name=message.from_user.first_name),
        reply_markup=keyboard
    )

@app.on_message(filters.command("help") & filters.private)
async def commands(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Open Commands Here", callback_data="HELP_BUTTON")]
        ]
    )

    await message.reply_text(HELP_TEXT, 
    reply_markup=InlineKeyboardMarkup(BUTTON),)
else:
    kb = InlineKeyboardMarkup(
        [
          [
            InlineKeyboardButton(
              "Click me for help", 
              url="https://t.me/CuteSerenaBot?start=help",
            ),
          ],
        ],
      )

   await message.reply_text(pm_text,
   reply_markup=kb,)
   add_group(message.chat.id)
pm_text = "Contact me in PM for help!"


@app.on_callback_query(filters.regex("help_back"))
async def help_back(_, query):
    await query.message.edit_text(HELP_TEXT, reply_markup=InlineKeyboardMarkup(BUTTON))

@app.on_callback_query(filters.regex("close"))
async def close(_, query):
    await query.message.delete()

@app.on_callback_query(filters.regex("admin_help"))
async def admin_help(_, query):
     await query.message.edit_text(ADMIN_TEXT, reply_markup=InlineKeyboardMarkup(BUTTON))

@app.on_callback_query(filters.regex("userinfo_help"))
async def userinfo_help(_, query):
     await query.message.edit_text(USERINFO_TEXT, reply_markup=InlineKeyboardMarkup(BUTTON))

@app.on_callback_query(filters.regex("misc_help"))
async def misc_help(_, query):
     await query.message.edit_text(MISC_TEXT, reply_markup=InlineKeyboardMarkup(BUTTON))

@app.on_callback_query(filters.regex("tagging_help"))
async def tagging_help(_, query):
     await query.message.edit_text(TAGGING_TEXT, reply_markup=InlineKeyboardMarkup(BUTTON))

@app.on_callback_query(filters.regex("fun_help"))
async def fun_help(_, query):
     await query.message.edit_text(FUN_TEXT, reply_markup=InlineKeyboardMarkup(BUTTON))
