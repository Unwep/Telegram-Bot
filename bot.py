from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
import asyncio
import keyboards as kb
import os

TOKEN = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message:Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    await message.answer(f"<b>Привет <a href='tg://user?id={user_id}'>{message.from_user.first_name}</a> , оставь свою заявку здесь\nи ожидай ответа</b>", parse_mode='HTML', reply_markup=kb.main)


@dp.callback_query(F.data == 'apply')
async def apply(callback: CallbackQuery):
    user_username = callback.from_user.username
    user_id = callback.from_user.id
    await callback.message.edit_text("<b>заявка успешно отправлена!\nОжидайте ответа 🫶🏻</b>", parse_mode='HTML')

    admin_message = (
        f'<b>Пользователь <a href="tg://user?id={user_id}">{callback.from_user.first_name}</a> оставил заявку в боте</b>')

    photo = FSInputFile("photo_2026-01-04_18-54-14.jpg")
    await bot.send_photo(
        chat_id = ADMIN_ID,
        photo = photo,
        caption = admin_message,
        parse_mode='HTML',
        reply_markup= await kb.get_url_open_chat(user_id)
    )

async def main():
    print("✅ Бот запущен")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("❗ Бот отключен")
