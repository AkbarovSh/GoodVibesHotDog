from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db_manager

admin_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Qidirish 🔎")
        ],
        [
            KeyboardButton(text="Hot-doglar 🌭"),
            KeyboardButton(text="Buyurtmalar 🛍"),
        ],
        [
            KeyboardButton(text="Statistikalar 📊"),
            KeyboardButton(text="Xabar yuborish ✍️"),
        ]
    ], resize_keyboard=True
)

admin_order_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="WAITING ⏳"),
            KeyboardButton(text="ACCEPTED ✅")
        ],
        [
            KeyboardButton(text="Statistics 📊"),
            KeyboardButton(text="CANCELED ❌")
        ],
        [
            KeyboardButton(text="Orqaga ⬅️")
        ],
    ], resize_keyboard=True
)

admin_back_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Orqaga ⬅️")
        ]
    ], resize_keyboard=True
)


async def admin_stickers_menu_def():
    stickers = db_manager.get_all_stickers()
    admin_stickers_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    add = KeyboardButton(text="Fast Food qo'shish ➕")
    back = KeyboardButton(text="Orqaga ⬅️")
    admin_stickers_menu.insert(back)
    admin_stickers_menu.insert(add)

    for sticker in stickers:
        keyboard = KeyboardButton(text=sticker[1])
        admin_stickers_menu.insert(keyboard)

    return admin_stickers_menu