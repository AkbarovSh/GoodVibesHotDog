from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import CHANNELS


async def user_product_buy_def(quantity, total):
    user_product_buy = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="➖", callback_data="minus_product"),
                InlineKeyboardButton(text=f"{quantity}/{total}", callback_data="popo"),
                InlineKeyboardButton(text="➕", callback_data="plus_product"),
            ],
            [
                InlineKeyboardButton(text="🛍 Savatni ko'rish", callback_data="show_basket"),
            ]
        ]
    )
    return user_product_buy


user_profile_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ism", callback_data="change_full_name"),
            InlineKeyboardButton(text="Raqam", callback_data="change_phone_number"),
        ]
    ]
)

user_basket_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛍 Zakaz berish", callback_data="order_basket"),
            InlineKeyboardButton(text="🧹 Savatni tozalash", callback_data="clear_basket"),
        ]
    ]
)


async def channels_keyboards(not_member: list):
    channels = InlineKeyboardMarkup(row_width=1)

    for link in not_member:
        button = InlineKeyboardButton(text=link['name'], url=link['url'])
        channels.insert(button)
    return channels