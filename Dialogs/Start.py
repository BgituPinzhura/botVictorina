from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton

import Dialogs.Registarion as Registration
from Database import database
from Callback import register_callback_kb, menu_callback_kb
import Dialogs.Settings as Settings
import Dialogs.Play as Play

router = Router()
router.include_router(Registration.router)
router.include_router(Settings.router)
router.include_router(Play.router)

kb = [[KeyboardButton(text="/play"),
       KeyboardButton(text="/settings")]]


@router.message(Command("start"))
async def handler_start(message: Message) -> None:
    if database.is_registered(message.from_user.id):
        await message.answer("Привет! Что хотим сделать?", reply_markup=menu_callback_kb)
        return
    await message.answer("Здарова! Это бот курсач с викторинами. Пожалуйста, пройдите регестрацию!\nНапиши /register",
                         reply_markup=register_callback_kb)


@router.callback_query(F.data == "старт")
async def callback_handler_start(callback: types.CallbackQuery):
    await callback.message.answer("Привет! Что хотим сделать?", reply_markup=menu_callback_kb)
    await callback.answer()
