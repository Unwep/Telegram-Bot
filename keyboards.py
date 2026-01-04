from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="оставить заявку", callback_data='apply')]
])


async def get_url_open_chat(user_id):
    builder = InlineKeyboardBuilder()
    builder.button(
        text='Перейти к диалогу',
        url=f'tg://openmessage?user_id={user_id}'
    )
    return builder.as_markup()
