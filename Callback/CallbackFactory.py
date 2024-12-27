from aiogram import types
from aiogram.types import InlineKeyboardMarkup

register_callback_kb = InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="Регистрация", callback_data="регистрация")]])

start_callback_kb = InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="Старт", callback_data="старт")]])

menu_callback_kb = InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="Играть", callback_data="играть"),
                      types.InlineKeyboardButton(text="Настройки", callback_data="настройки")]])

again_callback_kb = InlineKeyboardMarkup(
    inline_keyboard=[[types.InlineKeyboardButton(text="Еще раз", callback_data="играть"),
                      types.InlineKeyboardButton(text="Назад", callback_data="старт")]])
