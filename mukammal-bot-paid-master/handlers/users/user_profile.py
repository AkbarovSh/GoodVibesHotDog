from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile, CallbackQuery

from data.config import ADMINS
from keyboards.default.user_menu import user_product_menu, user_main_menu, user_order_menu, user_main_menu_back
from keyboards.inline.admin_keyboards import admin_order_decision_def
from keyboards.inline.user_keyboards import user_profile_menu, user_product_buy_def, user_basket_menu
from loader import dp, db_manager
from states.users import ProfileUpdate
from utils.random_number import get_random_id


@dp.message_handler(text="👤 Profile")
async def profile_menu_handler(message: types.Message):
    user = db_manager.get_user(message)
    if user:
        text = f"""
FI: {user[2]}
TEL: {user[3]}
GURUH TURI: {user[4]}
GURUH RAQAMI: {user[5]}
ID: {user[6]}
"""
        await message.answer(text=text, reply_markup=user_profile_menu)
    else:
        text = "Siz haqingizda ma'lumot topilmadi."
        await message.answer(text=text)


@dp.callback_query_handler(text="change_full_name")
async def change_full_name_handler(call: CallbackQuery):
    text = "Yangi ismni kiriting."
    await call.message.answer(text=text, reply_markup=user_main_menu_back)
    await ProfileUpdate.full_name.set()


@dp.message_handler(state=ProfileUpdate.full_name)
async def update_user_full_name(message: types.Message, state: FSMContext):
    if db_manager.update_user_profile(message, "full_name"):
        text = "Yangilandi."
    else:
        text = "Xatolik bor"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()