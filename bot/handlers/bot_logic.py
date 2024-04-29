from aiogram import types
from aiogram.types.web_app_info import WebAppInfo
from bot.core import dp


@dp.message_handler(commands=["start"])
async def info(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(
        types.KeyboardButton(
            "Открыть веб страницу",
            web_app=WebAppInfo(
                url="https://onesch.github.io/telegram-color-picker-bot/web.html"
            ),
        )
    )
    await message.answer("Привет", reply_markup=markup)
