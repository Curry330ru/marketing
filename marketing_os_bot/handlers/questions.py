from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.markdown import hbold

from gpt.generate import generate_hypotheses
from utils.timers import schedule_follow_up

class Form(StatesGroup):
    goal = State()
    niche = State()
    audience = State()


async def ask_goal(message: types.Message, state: FSMContext):
    await message.answer(f"{hbold('Какая у тебя цель?')} Напиши коротко")
    await state.set_state(Form.goal)
    schedule_follow_up(message.chat.id, message.answer)


async def goal_received(message: types.Message, state: FSMContext):
    await state.update_data(goal=message.text)
    await message.answer("В какой нише работаешь?")
    await state.set_state(Form.niche)
    schedule_follow_up(message.chat.id, message.answer)


async def niche_received(message: types.Message, state: FSMContext):
    await state.update_data(niche=message.text)
    await message.answer("Кто твоя аудитория и где ты их ищешь?")
    await state.set_state(Form.audience)
    schedule_follow_up(message.chat.id, message.answer)


async def audience_received(message: types.Message, state: FSMContext):
    data = await state.update_data(audience=message.text)
    ideas = await generate_hypotheses(data)
    await message.answer(ideas)
    await state.clear()


def register(dp):
    dp.message.register(goal_received, Form.goal)
    dp.message.register(niche_received, Form.niche)
    dp.message.register(audience_received, Form.audience)
