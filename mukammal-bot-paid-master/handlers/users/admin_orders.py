from aiogram import types

from aiogram.types import CallbackQuery

from data.config import ADMINS
from keyboards.inline.admin_keyboards import admin_order_decision_filter, admin_order_cancel, admin_order_decision_def, \
    admin_order_accepted_def, admin_order_accepted_filter, admin_order_canceled_filter
from loader import dp, db_manager, bot


@dp.callback_query_handler(admin_order_decision_filter.filter(action="admin_order_accept"), chat_id=ADMINS)
async def admin_order_accept_handler(call: CallbackQuery, callback_data: dict):
    order_id = int(callback_data.get("order_id"))
    user_id = int(callback_data.get("user_id"))

    if db_manager.update_order_status(order_id, "ACCEPTED"):
        text = f"🆔: {order_id}\nUshbu ID raqamli buyurtma qabul qilindi ✅"
    else:
        text = "Buyurtma qabul qilish jarayonida xatolik yuz berdi xo'jayin ❗️"

    await call.answer(text=text, show_alert=True)
    await bot.send_message(chat_id=user_id, text=text)


@dp.callback_query_handler(admin_order_cancel.filter(action="admin_order_cancel"), chat_id=ADMINS)
async def admin_order_accept_handler(call: CallbackQuery, callback_data: dict):
    order_id = callback_data.get("order_id")
    user_id = callback_data.get("user_id")

    if db_manager.update_order_status(order_id, "CANCELED"):
        text = f"🆔: {order_id}\nUshbu ID raqamli buyurtma qabul qilinmadi ❌"
    else:
        text = "Buyurtma qabul qilish jarayonida xatolik yuz berdi xo'jayin ❗️"

    await bot.send_message(chat_id=user_id, text=text)
    await call.answer(text=text, show_alert=True)



@dp.callback_query_handler(admin_order_accepted_filter.filter(action="admin_order_delivered"), chat_id=ADMINS)
async def admin_order_delivered_handler(call: CallbackQuery, callback_data: dict):
    order_id = callback_data.get("order_id")

    if db_manager.update_order_status(order_id, "DELIVERED"):
        text = f"🆔: {order_id}\nUshbu ID raqamli buyurtma yetkazib berildi ✅"
    else:
        text = "Buyurtma qabul qilish jarayonida xatolik yuz berdi xo'jayin ❗️"

    await bot.send_message(chat_id=user_id, text=text)
    await call.answer(text=text, show_alert=True)





@dp.callback_query_handler(admin_order_canceled_filter.filter(action="admin_order_canceled"), chat_id=ADMINS)
async def admin_order_canceled_handler(call: CallbackQuery, callback_data: dict):
    order_id = callback_data.get("order_id")

    if db_manager.update_order_status(order_id, "DELETED"):
        text = "Buyurtma o'chirildi ✅"
    else:
        text = "Buyurtmani o'chirish jarayonida xatolik yuz berdi xo'jayin ❗️"

    await call.answer(text=text, show_alert=True)





@dp.message_handler(text="⏳ WAITING", chat_id=ADMINS)
async def user_order_waiting_handler(message: types.Message):
    orders = db_manager.get_all_orders_by_status_admin("WAITING")

    if len(orders) == 0:
        text = "Hozirda buyurtmalar mavjud emas."
        await message.answer(text=text)
    else:
        for order in orders:
            order_items = db_manager.get_order_items_by_order_id(order[2])
            user = db_manager.get_user_by_id(order[1])
            products = ""
            counter = 1
            total_price = 0
            for item in order_items:
                total_price += float(item[4]) * float(item[3])
                products += f"<i><b>{counter})\t {item[2]}\t| {item[4]} ta\t| {item[3]} so'm\n</b></i>"
                counter += 1
            text = f"""
🆔 {order[2]}

☎️ {user[3]}
👤 {user[2]}
⏳ {order[3]}
⏰ {order[4]}
    
{products}
Jami: <b>{total_price} so'm</b>
"""
            await message.answer(text=text, reply_markup=await admin_order_decision_def(order[2], message.chat.id))


@dp.message_handler(text="✅ ACCEPTED", chat_id=ADMINS)
async def user_order_waiting_handler(message: types.Message):
    orders = db_manager.get_all_orders_by_status_admin("ACCEPTED")
    if len(orders) == 0:
        text = "Hozirda buyurtmalar mavjud emas."
        await message.answer(text=text)
    else:
        for order in orders:
            order_items = db_manager.get_order_items_by_order_id(order[2])
            user = db_manager.get_user_by_id(order[1])
            products = ""
            counter = 1
            total_price = 0
            for item in order_items:
                total_price += float(item[4]) * float(item[3])
                products += f"<i><b>{counter})\t {item[2]}\t| {item[4]} ta\t| {item[3]} so'm\n</b></i>"
                counter += 1
            text = f"""
🆔 {order[2]}

☎️ {user[3]}
👤 {user[2]}
⏳ {order[3]}
⏰ {order[4]}

{products}
Jami: <b>{total_price} so'm</b>
"""
            await message.answer(text=text, reply_markup=await admin_order_accepted_def(order[2], message.chat.id))