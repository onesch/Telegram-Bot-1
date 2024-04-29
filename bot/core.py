import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from bot.token import TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())
logging.info("LoggingMiddleware успешно установлен✅")
