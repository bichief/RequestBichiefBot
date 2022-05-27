from sqlalchemy import update, select, func
from sqlalchemy.exc import IntegrityError

from utils.db_api.base import async_sessionmaker
from utils.db_api.models.users import User


async def add_user(telegram_id):
    try:
        async with async_sessionmaker() as session:
            await session.merge(User(telegram_id=telegram_id))
            await session.commit()
    except IntegrityError:
        return True


async def select_users():
    array = []
    async with async_sessionmaker() as session:
        result = select(User.telegram_id)
        finish = await session.execute(result)
        for row in finish.scalars():
            array.append(row)

        return array
