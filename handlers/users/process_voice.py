from aiogram import types
from aiogram.dispatcher.filters import Text

from data.config import ADMINS
from loader import dp, bot


# Здесь мы ловим нажатие на кнопку
@dp.callback_query_handler(Text(equals='create_voice'))
async def creating_voice(call: types.CallbackQuery):
    # Редактируем сообщение
    await call.message.edit_text('🧑🏼‍💻 <b>Отлично!</b>\n'
                                 'Заявка успешно создана.\n'
                                 'В скором времени с вами свяжутся, <b>хорошего дня</b>!')

    # Отправляем сообщение разработчикам
    await bot.send_message(
        chat_id=ADMINS,
        text='📍 Пришла новая заявка!\n\n'
             f'Заявщик - @{call.from_user.username}\n'
             f'<b>Спишитесь в личке для уточнения.</b>'
    )