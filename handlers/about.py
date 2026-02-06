from aiogram import Bot, types, Router
from aiogram.filters import Command

from sqlalchemy.ext.asyncio import AsyncSession


info_router = Router()


f'''
Чтобы не захламлять хендлеры, то выносим текст о направлениях в отдельный файл texts.py
в папку utils
'''
