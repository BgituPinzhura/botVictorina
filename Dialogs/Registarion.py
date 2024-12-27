from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from Callback import start_callback_kb

import Dialogs.Difficult_Builder as Difficult_Builder

from Database import database

router = Router()


class Form(StatesGroup):
    registration_question_type_choosing = State()


@router.callback_query(F.data.lower() == "регистрация")
async def registration(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await registration_handler(callback.message, state)


@router.message(Command("register"))
async def registration_handler(message: Message, state: FSMContext) -> None:
    if database.is_registered(telegram_id=message.from_user.id):
        await message.answer("Вы уже зарегестрированы!", reply_markup=start_callback_kb)
        return
    await message.answer("Выберите уровень сложности вопросов: ",
                         reply_markup=Difficult_Builder.keyboard)
    await state.set_state(Form.registration_question_type_choosing)


@router.message(Form.registration_question_type_choosing)
async def question_type_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(question_type=message.text)
    question_type = await state.get_data()
    database.registration(message.from_user.id, question_type["question_type"])
    await message.answer("Спасибо за регистрацию!", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Можно начинать игру!", reply_markup=start_callback_kb)
    await state.clear()
