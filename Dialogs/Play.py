from aiogram import Router, F, types
from aiogram.types import InlineKeyboardMarkup

from Callback.CallbackFactory import again_callback_kb

from Game import game
from Database import database
from random import shuffle

router = Router()


@router.callback_query(F.data.lower() == "играть")
async def start_game(callback: types.CallbackQuery):
    victorina = game(database, str(callback.from_user.id))
    question = victorina.get_question()
    answers = victorina.get_answers()
    shuffle(answers)
    btn1 = types.InlineKeyboardButton(text=answers[0][1], callback_data="ans_" + str(answers[0][0]))
    btn2 = types.InlineKeyboardButton(text=answers[1][1], callback_data="ans_" + str(answers[1][0]))
    btn3 = types.InlineKeyboardButton(text=answers[2][1], callback_data="ans_" + str(answers[2][0]))
    btn4 = types.InlineKeyboardButton(text=answers[3][1], callback_data="ans_" + str(answers[3][0]))
    btn5 = types.InlineKeyboardButton(text="В меню", callback_data="старт")
    kb = InlineKeyboardMarkup(inline_keyboard=[[btn1, btn2], [btn3, btn4], [btn5]])
    await callback.message.answer(question, reply_markup=kb)
    await callback.answer()


@router.callback_query(F.data.startswith("ans_"))
async def win_condition(callback: types.CallbackQuery):
    if callback.data[4:] == "0":
        await callback.message.answer("Вы угадали!", reply_markup=again_callback_kb)
        await callback.answer()
        return
    await callback.message.answer("Вы не угадали :(\nПопробуйте еще раз!", reply_markup=again_callback_kb)
    await callback.answer()
    
