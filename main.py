from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
import Function_bd
import markup






token = "6592140370:AAE0k034z0P0g0ScGFDBnCyhbosXtOOtYXg"
bot = Bot(token)
dp = Dispatcher(bot)
#***********************************************************************************************************************
@dp.message_handler(commands=["start"])
async def start_message(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,text="Здравствуйте, вас приветствует ваш персанальный помошник по контенту!"
                                                        "Здесь вы можете настроить парсинг контента в свой канал "
                                                        "ручное отправление готовых постов\n"
                                                        "Так же доступны функции такие как:\n"
                                                        " -Автоотправка контента к вам в канал\n"
                                                        " -перевод постов на другие языки\n"
                                                        " -отсылка готовых постов из бота в канал\n"
                                                        " -создание топов по статистике просмотра за день\n"
                                                        " - ведение статистики канала + анализ контента\n")

    await  bot.send_message(chat_id=message.chat.id, text="По всем вопросам можете обращаться @Eduard_wer", reply_markup=markup.welcom_markup)
    #работа с бд

#*****************************************************************************************************************************************************

@dp.message_handler(commands=["add_my_groups"])
async  def add_function(message:types.Message):
    message_ = message.text.split('/add_my_groups')
    print(message_[1])
    #Работа с бд
    # Тут будет функция из function_bot для добавления id групп пользователя
    await bot.send_message(chat_id=message.chat.id,text=f"Вы добавили группу {message_[1]}")

#***********************************************************************************************************************
@dp.message_handler(commands=["add_pars_groups"])
async  def add_function(message:types.Message):
    message_ = message.text.split('/add_pars_groups')
    print(message_[1])
    #Работа с бд
    await bot.send_message(chat_id=message.chat.id,text=f"Вы добавили группу {message_[1]}")

#*************************************************************************************************************************
@dp.message_handler(commands=["send"])
async def send_messages(message:types.Message):
    if message.content_type == "text":
        text = message.text.split("/send")
        #работа с бд
        value = value.split(",")
        value = list(value)
        if value[0] != "None":
            for group in value:
                await bot.send_message(chat_id=group, text=text[1])
            await bot.send_message(message.chat.id, text="Рассылка сделанна")
        else:
            await bot.send_message(chat_id=message.chat.id, text="Вы не добавили группы!!")

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def send_photo(message:types.Message):
        photo = message.photo[-1].file_id if message.photo else None
        text = message.caption
        value = await function_bot.check_cell_value(user_id=message.chat.id, column_name="my_groups")
        value = value.split(",")
        value = list(value)
        if value[0] != "None":
            for group in value:
                await bot.send_photo(chat_id=group, caption=text,photo=photo)
            await bot.send_message(message.chat.id, text="Рассылка сделанна")
        else:
            await bot.send_message(chat_id=message.chat.id, text="Вы не добавили группы!!")

#**********************************************************************************************************************
@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def send_photo(message:types.Message):
        text = message.caption
        value = await function_bot.check_cell_value(user_id=message.chat.id, column_name="my_groups")
        value = value.split(",")
        value = list(value)
        if value[0] != "None":
            for group in value:
                await bot.send_video(chat_id=group,video=message.video.file_id,caption=text)
            await bot.send_message(message.chat.id, text="Рассылка сделанна")
        else:
            await bot.send_message(chat_id=message.chat.id, text="Вы не добавили группы!!")

#***********************************************************************************************************************
@dp.message_handler()
async def all_message(message:types.Message):
    text = message.text
    match message.text:
        case "Ваш аккаунт":
            privileg_= await function_bot.check_cell_value(user_id=message.chat.id,column_name='privileg')
            #pars_group_ = await function_bot.check_cell_value(user_id=message.chat.id,column_name='pars_group')
            my_group = await function_bot.check_cell_value(user_id=message.chat.id,column_name='my_groups')

            await bot.send_message(chat_id=message.chat.id,text=f"Ваш аккаунт {message.chat.username} \n"#Добавить приветствие
                                                                f"ID Групп для рассылки: {my_group} \n"
                                                                f"ID Групп для парсинга:  \n"# доделать парс групп
                                                                f"Ваша привелегия: {privileg_}\n"
                                                                f"Ваш ID: {message.chat.id}")#Добавить список групп для рассылки


        case "Инструкция":
            pass # Написать инструкцию для особо одарённых
        case "Пользовательское соглашение":
            pass #Написать пользовательское соглашение
        case "Статистика канала":
            pass # Написать код для генерации статистики
        case "Доп. Функции":
            await bot.send_message(chat_id=message.chat.id,text="Уже скоро!!\n"
                                                                "Наша команда в работе!")
        case _:
            my_groups= await function_bot.check_cell_value(user_id=message.chat.id,column_name="my_groum")

#***********************************************************************************************************************


executor.start_polling(dp,skip_updates=True)