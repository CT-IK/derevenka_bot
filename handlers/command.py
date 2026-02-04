from aiogram import Bot, types, Router
from aiogram.filters import Command

from sqlalchemy.ext.asyncio import AsyncSession

command_router = Router()


@command_router.message(Command('user_id'))
async def get_user_id_cmd(message:types.Message):
    user_id = message.from_user.id
    await message.answer(f'Твой телеграм ID: {user_id}')


@command_router.message(Command('chat_id'))
async def get_chat_id_cmd(message: types.Message):
    chat_id= message.chat.id
    await message.answer(f'Вот твой ID этого чата: {chat_id}')


@command_router.message(Command('about'))
async def about_cmd(message:types.Message):
    

    await message.answer('Выводим тут инфу о нашем комитете')



# TODO: Возможно стоит подумать над таро раскладом как /command