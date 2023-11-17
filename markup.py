from  aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
#                         Главное меню (появляется при запуске бота)
politic_ = KeyboardButton("Пользовательское соглашение")
statisty = KeyboardButton("Статистика канала")
function_ = KeyboardButton("Доп. Функции")
acaunt = KeyboardButton("Ваш аккаунт")
lessons = KeyboardButton("Инструкция")
welcom_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(politic_,statisty,function_,acaunt,lessons)
#**************************************************************************************************************************
