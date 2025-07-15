import asyncio
from typing import Callable, Dict

_follow_tasks: Dict[int, asyncio.Task] = {}


def schedule_follow_up(chat_id: int, answer: Callable[[str], None]) -> None:
    async def send_tip():
        await asyncio.sleep(60)
        await answer("Пока ты перевариваешь — вот совет на подумать 👇")
    _follow_tasks[chat_id] = asyncio.create_task(send_tip())
