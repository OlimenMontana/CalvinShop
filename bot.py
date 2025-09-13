import os
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv("TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID", "0"))

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

CATALOG = {'item1': {'title': 'Шишки АК-47', 'weight': '1.0г', 'price': '400 инди, 450 сатива грн'}, 'item2': {'title': 'Гашиш АФГАН', 'weight': '1.0г', 'price': '500 грн'}, 'item3': {'title': 'Киф АФГАН', 'weight': '1.0г', 'price': '600 грн'}, 'item4': {'title': 'Амфетамин VHQ', 'weight': '1.0г', 'price': '700 грн'}, 'item5': {'title': 'Мефедрон VHQ', 'weight': '1.0г', 'price': '700 грн'}, 'item6': {'title': 'Метадон Уличный', 'weight': '1.0г', 'price': '800 грн'}, 'item7': {'title': 'Экстази Домино', 'weight': '1 шт', 'price': '450 грн'}, 'item8': {'title': 'Грибы', 'weight': '1.0г', 'price': '450 грн'}, 'item9': {'title': 'ЛСД-300', 'weight': '1 шт.', 'price': '500 грн'}, 'item10': {'title': 'МДМА', 'weight': '1.0г', 'price': '500 грн'}, 'item11': {'title': 'Alfa pvp', 'weight': '1.0г', 'price': '600 грн'}, 'item12': {'title': 'Гер', 'weight': '0.5г', 'price': '900 грн'}, 'item13': {'title': 'Винт', 'weight': '5мг', 'price': '1200 грн'}, 'item14': {'title': 'Мушрум', 'weight': '1шт', 'price': '450 грн'}, 'item15': {'title': 'Кетамин', 'weight': '1.0г', 'price': '500 грн'}, 'item16': {'title': 'D-mesth', 'weight': '0.25г', 'price': '600 грн'}, 'item17': {'title': 'Кокаїн', 'weight': '0.25г', 'price': '1000 грн'}}

@dp.message_handler(commands=["start", "menu"])
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    for key, item in CATALOG.items():
        kb.add(types.InlineKeyboardButton(f"{item['title']} | {item['weight']} | {item['price']}", callback_data=f"buy:{key}"))
    await message.answer("👋 Привет! Выберите товар:", reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data.startswith("buy:"))
async def buy(call: types.CallbackQuery):
    item_id = call.data.split(":")[1]
    item = CATALOG[item_id]
    text = (
        f"🛒 Вы выбрали: {item['title']}\n"
        f"⚖ Вес: {item['weight']}\n"
        f"💰 Цена: {item['price']}\n\n"
        "Для оплаты переведите сумму на карту:\n\n"
        "`5355 2800 2484 3821`\n"
        "Получатель: Иван Иванов\n\n"
        "📌 В комментарии укажите ваш @username\n"
        "После оплаты пришлите скриншот чека сюда."
    )
    await call.message.answer(text, parse_mode="Markdown")
    if ADMIN_CHAT_ID:
        await bot.send_message(ADMIN_CHAT_ID, f"Новый заказ: {call.from_user.id} выбрал {item['title']} ({item['weight']}, {item['price']})")
    await call.answer()

@dp.message_handler(content_types=["photo"])
async def receive_check(message: types.Message):
    if ADMIN_CHAT_ID:
        await bot.send_message(ADMIN_CHAT_ID, f"Чек от {message.from_user.id}")
        await message.forward(ADMIN_CHAT_ID)
    await message.reply("✅ Спасибо! Мы проверим оплату и свяжемся с вами.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
