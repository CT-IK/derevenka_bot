from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.crud import get_or_create_user
from database.engine import get_session

start_router = Router()

@start_router.message(CommandStart())
async def start_handler(message: Message):
    user_id = message.from_user.id
    async for session in get_session():
        user = await get_or_create_user(session, user_id)
        
        if user:
            await message.answer("Ваш Telegram ID записан в базу данных!")
        else:
            await message.answer("Вы уже зарегистрированы!")


# get_sqlite_session -> что-то простенькое
# get_postgres_session -> что-то серьезное