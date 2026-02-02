import asyncio
import logging

from bot import bot, dp
from config import BOT_TOKEN  # Не используется напрямую, но для примера
from database.engine import create_db

# Настройка логирования
logging.basicConfig(level=logging.INFO)

async def main():
    await create_db()  # Создаём таблицы, если их нет
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())