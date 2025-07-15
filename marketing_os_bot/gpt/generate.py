import os
from openai import OpenAI

from .phrases import PHRASES, RESERVE_IDEA

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT = """Ты инициативный маркетолог. Дай 5 идей по продвижению для ниши {niche}.
"""

async def generate_hypotheses(data: dict) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": PROMPT.format(niche=data.get('niche'))}],
        )
        text = response.choices[0].message.content.strip()
        if not text:
            text = RESERVE_IDEA
        phrase = PHRASES[0]
        return f"<b>{phrase}</b>\n{text}"
    except Exception:
        return "Хм, не сработало. Давай попробуем ещё раз?"
