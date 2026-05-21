import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "8943722990:AAH184Z8Dxl6kyuqAxpnxmeO8Mtpqy7DGhc"
FROM_CHANNEL = -1003923130956   # Klientlar kanali/guruhi
TO_CHANNEL = -5207048723        # Taksistlar kanali

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def is_admin(chat_id, user_id):
    try:
        member = await bot.get_chat_member(chat_id, user_id)
        return member.status in ['administrator', 'creator']
    except:
        return False

@dp.message_handler(content_types=types.ContentTypes.ANY, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def handle_group(message: types.Message):
    if message.chat.id != FROM_CHANNEL:
        return

    user = message.from_user

    # Admin bo'lsa, qo'tirmamiz
    if await is_admin(message.chat.id, user.id):
        return

    # Taksistlarga yuborish
    admin_msg = (
        f"🚖 *YANGI BUYURTMA*\n"
        f"{'─' * 28}\n"
        f"👤 {user.full_name}\n"
        f"🆔 @{user.username or 'username yoq'}\n"
        f"{'─' * 28}\n"
        f"💬 {message.text or 'Matn yoq'}"
    )
    await bot.send_message(TO_CHANNEL, admin_msg, parse_mode="Markdown")

    # Klient xabarini o'chirish
    try:
        await message.delete()
    except:
        pass

    # O'rniga bot xabari yozish
    await bot.send_message(
        FROM_CHANNEL,
        f"🚖 *{user.full_name}* ning buyurtmasi qabul qilindi!\n\n"
        "Shofyorlarimiz tez orada bog'lanadi! 😊",
        parse_mode="Markdown"
    )

@dp.channel_post_handler(content_types=types.ContentTypes.ANY)
async def handle_channel(message: types.Message):
    if message.chat.id == FROM_CHANNEL:
        await message.forward(TO_CHANNEL)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
