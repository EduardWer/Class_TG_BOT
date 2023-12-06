from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor

import Function_bd
import markup

db = Function_bd.Database(db_file='db.sqlite')

token = "6592140370:AAE0k034z0P0g0ScGFDBnCyhbosXtOOtYXg"
bot = Bot(token)
dp = Dispatcher(bot)
#***********************************************************************************************************************
@dp.message_handler(commands=["start"])
async def start_message(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="Здравствуйте, вас приветствует ваш персанальный помощник по контенту!"
                                                        "Здесь вы можете настроить парсинг контента в свой канал "
                                                        "ручное отправление готовых постов\n"
                                                        "Так же доступны функции такие как:\n"
                                                        " -Автоотправка контента к вам в канал\n"
                                                        " -перевод постов на другие языки\n"
                                                        " -отсылка готовых постов из бота в канал\n"
                                                        " -создание топов по статистике просмотра за день\n"
                                                        " - ведение статистики канала + анализ контента\n")

    await  bot.send_message(chat_id=message.chat.id, text="По всем вопросам можете обращаться @Eduard_wer", reply_markup=markup.welcom_markup)
    db.add_user(user_id=message.chat.id,user_name=message.chat.username)
#*****************************************************************************************************************************************************

@dp.message_handler(commands=["add_my_groups"])
async  def add_function(message:types.Message):
    message_ = message.text.split('/add_my_groups ')
    if message_[1] == '':
       await bot.send_message(message.chat.id,"Неверная команда")
    else:

        try:
            message_ = str(message_[1])
            db.add_my_groups(user_id=message.chat.id, Udata=message_)
            await bot.send_message(chat_id=message.chat.id,text=f"Вы добавили группу {message_[1]}")
        except:
            await bot.send_message(message.chat.id,"Вы ввели не допустимое значение!!")

#***********************************************************************************************************************
@dp.message_handler(commands=["add_pars_groups"])
async  def add_function(message:types.Message):
    message_ = message.text.split('/add_pars_groups')
    print(message_[1])
    db.add_Pars_groups(message_[1], message.chat.id)
    await bot.send_message(chat_id=message.chat.id,text=f"Вы добавили группу {message_[1]}")


@dp.message_handler(commands=["translate"])
async def translate_message(message: types.Message):
   await bot.send_message(message.chat.id, "Тут вы можете перевести пост")

#*************************************************************************************************************************
@dp.message_handler(commands=["send"])
async def send_messages(message:types.Message):
    user_id = message.chat.id
    if message.content_type == "text":
        text = message.text.split("/send")
        value = db.send_defult_query(query='SELECT my_groum FROM Users where user_id=?', data=user_id)


        if value != None:

            for group in value:
                await bot.send_message(chat_id=group, text=text[1])
            await bot.send_message(message.chat.id, text="Рассылка сделанна")
        else:
            await bot.send_message(chat_id=message.chat.id, text="Вы не добавили группы!!")

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def send_photo(message:types.Message):
        photo = message.photo[-1].file_id if message.photo else None
        text = message.caption
        db.apdate_data(table='Content', column="Foto_id", indef_column="Content_id", user_id=message.chat.id,
                       data=message.photo[-1].file_id)
        db.apdate_data(table='Content', column="caption", indef_column="Content_id", user_id=message.chat.id,
                       data=text)
        value = db.send_defult_query(query='SELECT my_groum FROM Users where user_id=?', data=message.chat.id)
        try:
         if value != None:
            for group in value:
                await bot.send_photo(chat_id=group, caption=text,photo=photo)
            await bot.send_message(message.chat.id, text="Рассылка сделанна")
         else:
            await bot.send_message(chat_id=message.chat.id, text="Вы не добавили группы!!")
        except:
            await  bot.send_message(chat_id=message.chat.id, text="Вы не добавили группу")

#**********************************************************************************************************************
@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def send_photo(message:types.Message):
        text = message.caption
        db.apdate_data(table='Content', column="Video_id", indef_column="Content_id", user_id=message.chat.id,
                       data=message.video.file_id)
        value = db.send_defult_query(query='SELECT my_groum FROM Users where user_id=?', data=message.chat.id)
        if value != None:
            for group in value:
                await bot.send_video(chat_id=group,video=message.video.file_id,caption=text)
            await bot.send_message(message.chat.id, text="Рассылка сделанна")
        else:
            await bot.send_message(chat_id=message.chat.id, text="Вы не добавили группы!!")

#***********************************************************************************************************************
@dp.message_handler()
async def all_message(message:types.Message):
    match message.text:
        case "Ваш аккаунт":
            privileg_= db.send_defult_query(query='SELECT privileg FROM Users WHERE user_id=?',data=message.chat.id)
            pars_group_ = db.send_query(query='SELECT Group_id FROM Content WHERE Content_id=?',data=message.chat.id)
            my_group = db.send_query(query='SELECT my_groum FROM Users where user_id=?', data=message.chat.id)

            await bot.send_message(chat_id=message.chat.id,text=f"Ваш аккаунт {message.chat.username} \n"#Добавить приветствие
                                                                f"ID Групп для рассылки: {my_group} \n"
                                                                f"ID Групп для парсинга: {pars_group_} \n"# доделать парс групп
                                                                f"Ваша привелегия: {privileg_[0]}\n"
                                                                f"Ваш ID: {message.chat.id}")#Добавить список групп для рассылки

        case "Инструкция":
            await bot.send_message(message.chat.id, "C инструкцией мы можете ознакомиться в нашем Ютуб канале")
        case "Пользовательское соглашение":
            await bot.send_message(message.chat.id,"Внимательно ознакомтесь с условиями пользования")
            file_path  = 'sogloshenie/Пользовательское_соглашение_сервисов_PremSq.docx'
            with open(file_path,'rb') as file:
                await bot.send_document(chat_id=message.chat.id,document=file)
        case "Статистика канала":
            await bot.send_message(message.chat.id,"Статистику каналов вы можете посмотреть на нашем сайте !!\n"
                                                   "https://Premium_product.ru")
        case "Доп. Функции":
            await bot.send_message(chat_id=message.chat.id,text='Конечно!',reply_markup=markup.set_groups)
        case "Удалить мои группы":
            db.apdate_data(table='Users',column='my_groum',indef_column='user_id',data=None,user_id=message.chat.id)
        case 'Удалить парс. группы':
            db.apdate_data(table='Content', column='Group_id', indef_column='Content_id', data=None, user_id=message.chat.id)
        case "Назад":
            await bot.send_message(message.chat.id,'Хорошо!',reply_markup=markup.welcom_markup)
        case _:
            type_contert = message.content_type
            match type_contert:
                case "text":
                    db.apdate_data(table='Content', column="Content_text", indef_column="Content_id",
                                   user_id=message.chat.id, data=message.text)


#***********************************************************************************************************************

executor.start_polling(dp,skip_updates=True)