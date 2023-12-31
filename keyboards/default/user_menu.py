from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db_manager

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌭 Hot-doglar"),
            KeyboardButton(text="🛍 Mening buyurtmalarim"),
        ],
        [
            KeyboardButton(text="📞 Contact"),
            KeyboardButton(text="👤 Profil"),
        ]
    ], resize_keyboard=True
)

user_product_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎥 Anime"),
            KeyboardButton(text="👨‍💻 Coding")
        ],
        [
            KeyboardButton(text="😻 Cats"),
            KeyboardButton(text="🎲 Game")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga")
        ],
    ], resize_keyboard=True
)



user_order_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏳ WAITING"),
            KeyboardButton(text="✅ ACCEPTED")
        ],
        [
            KeyboardButton(text="📊 Statistics"),
            KeyboardButton(text="❌ CANCELED")
        ],
        [
            KeyboardButton(text="⬅️ Orqaga")
        ],
    ], resize_keyboard=True
)

user_main_menu_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ], resize_keyboard=True
)


async def user_stickers_menu_def():
    stickers = db_manager.get_all_stickers()
    admin_stickers_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    back = KeyboardButton(text="⬅️ Orqaga")
    admin_stickers_menu.insert(back)

    for sticker in stickers:
        keyboard = KeyboardButton(text=sticker[1])
        admin_stickers_menu.insert(keyboard)

    return admin_stickers_menu