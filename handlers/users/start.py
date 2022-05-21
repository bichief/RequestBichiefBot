import asyncio

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import md

from keyboards.inline.create_voice import voice_keyboard
from loader import dp, bot


# Обработчик комманды /start
@dp.message_handler(CommandStart())
async def start_cmd(message: types.Message):
    if message.get_args() != '':
        # Отправляем "Печатает..." в переписку
        await bot.send_chat_action(
            chat_id=message.chat.id,
            action=types.ChatActions.TYPING
        )
        # Задержка в 1.5 секунды, дабы создавалось ощущение будто тебе кто-то пишет))
        await asyncio.sleep(1.5)

        # Отправляем первое сообщение пользователю
        await message.answer(f'🧑🏼‍💻 Привет, <b>{message.from_user.username}</b>!\n'
                             f'Перед отправкой заявки, ознакомься с полезной информацией.')

        await bot.send_chat_action(
            chat_id=message.chat.id,
            action=types.ChatActions.TYPING
        )
        await asyncio.sleep(1.5)

        await message.answer('🧑🏼‍💻 <i>Мы</i> — команда разработчиков.\n'
                             'Занимаемся разработкой ботов для <b>Telegram</b>.\n\n'
                             'В наш спектр предоставляемых услуг входит создание маркетплейсов, парсеров, гарант-ботов и '
                             'многого другого, что собственно будет необходимо заказчику.')

        await bot.send_chat_action(
            chat_id=message.chat.id,
            action=types.ChatActions.TYPING
        )
        await asyncio.sleep(4)

        await message.answer('🧑🏼‍💻 <b> Из чего формируется цена?</b>\n\n'
                             'В большей части цена за проект формируется следующим образом:\n'
                             '<b>- сложность проекта\n'
                             '- ориентировочное время выполнения\n'
                             '- наличие персональной скидки</b>')

        await bot.send_chat_action(
            chat_id=message.chat.id,
            action=types.ChatActions.TYPING
        )
        await asyncio.sleep(2)

        await message.answer('🧑🏼‍💻 <b>А отзывы есть?</b>\n\n'
                             '"Вставать на рынок" без отзывов - трудная задача.\n'
                             f'Наши же вы можете посмотреть в — {md.hlink(url="t.me/bichief_otzivi", title="канале")}',
                             disable_web_page_preview=True)

        await bot.send_chat_action(
            chat_id=message.chat.id,
            action=types.ChatActions.TYPING
        )
        await asyncio.sleep(2)

        # Финальное сообщение с клавиатурой. Путь до клавиатуры keyboards -> inline -> create_voice.py
        await message.answer('🧑🏼‍💻 <b>Ознакомившись с информацией</b>,\n'
                             'Вы можете оставить свою заявку.', reply_markup=voice_keyboard)
    else:
        await message.answer('🧑🏼‍💻 <b>Вы можете оставить свою заявку.</b>', reply_markup=voice_keyboard)
