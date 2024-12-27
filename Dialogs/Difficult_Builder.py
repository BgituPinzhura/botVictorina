from aiogram import types

kb = [[types.KeyboardButton(text="1"),
      types.KeyboardButton(text="2")],
      [types.KeyboardButton(text="3"),
      types.KeyboardButton(text="4")]]

keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Введите уровень сложности:"
)
