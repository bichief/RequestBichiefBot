# Тут хранится единственная клавиатура, которая отслывается пользовалю
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

voice_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='📍 Оставить заявку', callback_data='create_voice')
    ]
]
)
