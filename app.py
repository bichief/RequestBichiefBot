from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.db_api.base import init_db
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    # Уведомление о запуке/рестарте
    await on_startup_notify(dispatcher)
    # Подключаемся к БД
    await init_db()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
