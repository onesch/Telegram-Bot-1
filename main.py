from aiogram import executor
from bot.core import dp
from bot.handlers import bot_logic

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
