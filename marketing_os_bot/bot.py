import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv

from utils.logger import setup_logger
from handlers import questions, responses, errors

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not TELEGRAM_TOKEN:
    raise SystemExit("TELEGRAM_TOKEN is missing")

if not OPENAI_API_KEY:
    raise SystemExit("OPENAI_API_KEY is missing")

logger = setup_logger()

bot = Bot(TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

async def start_handler(message: types.Message):
    await message.answer(
        f"{hbold('Привет!')} Я помогу тебе с маркетингом. Давай начнем?",
    )
    await questions.ask_goal(message, state=None)


dp.message.register(start_handler, CommandStart())
questions.register(dp)
responses.register(dp)
errors.register(dp)


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
