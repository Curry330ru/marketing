from aiogram import types


async def unknown_button(message: types.Message):
    await message.answer("Давай сначала разберёмся, что ты хочешь достичь 🙌")


def register(dp):
    dp.message.register(unknown_button, lambda m: m.text.startswith('/'), flags={"unhandled": True})
