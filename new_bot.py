import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "8943722990:AAH184Z8Dxl6kyuqAxpnxmeO8Mtpqy7DGhc"
ADMIN_GROUP = -5207048723

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def handle_message(message: types.Message):
    user = message.from_user

    # Guruhga yuborish
    admin_msg = (
        f"🚖 *YANGI BUYURTMA*\n"
        f"{'─' * 28}\n"
        f"👤 {user.full_name}\n"
        f"🆔 @{user.username or 'username yoq'}\n"
        f"📱 ID: {user.id}\n"
        f"{'─' * 28}\n"
        f"💬 {message.text or 'Matn yoq'}"
    )
    await bot.send_message(ADMIN_GROUP, admin_msg, parse_mode="Markdown")

    # Klientga javob
    await message.answer(
        "🚖 *Shofyorlarimiz siz bilan tezda aloqaga chiqadi!*\n\n"
        "Xizmatimizga ishonch uchun rahmat! 😊",
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
