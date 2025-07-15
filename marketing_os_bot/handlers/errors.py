from aiogram import types
from aiogram.exceptions import TelegramNetworkError


async def errors_handler(event: types.ErrorEvent):
    if isinstance(event.exception, TelegramNetworkError):
        await event.update.message.answer("Хм, не сработало. Давай попробуем ещё раз?")


def register(dp):
    dp.errors.register(errors_handler)
