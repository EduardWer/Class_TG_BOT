from  aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
#                         Главное меню (появляется при запуске бота)
politic_ = KeyboardButton("Пользовательское соглашение")
statisty = KeyboardButton("Статистика канала")
function_ = KeyboardButton("Доп. Функции")
acaunt = KeyboardButton("Ваш аккаунт")
lessons = KeyboardButton("Инструкция")
welcom_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(politic_,statisty,function_,acaunt,lessons)
#**************************************************************************************************************************

del_my_group=KeyboardButton("Удалить мои группы")
del_pars_group=KeyboardButton("Удалить парс. группы")
deck = KeyboardButton('Назад')
set_groups = ReplyKeyboardMarkup(resize_keyboard=True).add(del_my_group,del_pars_group,deck)
