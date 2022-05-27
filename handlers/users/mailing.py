from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BotBlocked

from data import config
from loader import dp, bot
from states.mailing import Mail
from utils.db_api.commands.users import select_users


@dp.message_handler(Command('send'), user_id=config.ADMINS)
async def mailing_first(message: types.Message):
    await message.answer('Введите сообщение для рассылки.')
    await Mail.first()


@dp.message_handler(state=Mail.mess)
async def mailing_finish(message: types.Message, state: FSMContext):
    await state.reset_state()
    text = message.text

    users = await select_users()

    counter = 0
    non_counter = 0

    for user in users:
        try:
            await bot.send_message(
            chat_id=user,
            text=text
            )
            counter += 1
        except BotBlocked:
            non_counter += 1


    await message.answer(f'Сообщение было доставлено {counter} человек\n'
                         f'Не получили - {non_counter} :c')
