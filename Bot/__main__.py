from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot import app 

if __name__ == "__main__":
    app.run()
    with app:
       app.send_photo(
        chat_id=-1002085445813,
        photo="https://telegra.ph/file/40b478d7e9c0a7df55881.jpg",
        caption="Bot Has Been Started",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support", url="https://t.me/+tqQMRvR0NiMyZTg1")]])
       )
