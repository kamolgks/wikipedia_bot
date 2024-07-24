import logging
from os import getenv
from asyncio import run
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from handlers import handlers

load_dotenv()

async def main():
    dp = Dispatcher()
    dp.include_router(handlers.router)

    TOKEN = getenv('BOT_TOKEN')
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        run(main())
    except Exception as e:
        raise(f'{e}')
