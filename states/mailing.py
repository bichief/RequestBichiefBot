from aiogram.dispatcher.filters.state import StatesGroup, State


class Mail(StatesGroup):
    mess = State()