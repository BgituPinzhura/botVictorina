from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from Callback import start_callback_kb

from Database import database

from Dialogs.Difficult_Builder import keyboard

router = Router()


class Form(StatesGroup):
    question_type_choosing = State()


@router.callback_query(F.data == "настройки")
async def callback_settings(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Изменить уровень сложности:", reply_markup=keyboard)
    await state.set_state(Form.question_type_choosing)


@router.message(Form.question_type_choosing)
async def choose_question_type(message: Message, state: FSMContext):
    await state.update_data(question_type=message.text)
    question_type = await state.get_data()
    database.set_question_type(question_type["question_type"], message.from_user.id)
    await message.answer("Сложность изменена!", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Можете играть!", reply_markup=start_callback_kb)
