import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("token")

def telegram_bot(token):
    bot = telebot.TeleBot(token)


    @bot.message_handler(commands=["start"])  # Делаем старт
    def start(message):
        mess = f'Привет, {message.from_user.first_name}'
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)  # Создаём кнопки при старте
        help_bt = types.KeyboardButton("Помощь")  # Кнопка помощи

        murkup.add(help_bt)  # Добавляем кнопки
        bot.send_message(message.chat.id, mess, reply_markup=murkup)  # Отправляем в чат


    @bot.message_handler(commands=["contacts"]) # Контакты
    def cont(message):
        markup = types.InlineKeyboardMarkup()
        narochguesthouse_by = types.InlineKeyboardButton("Наш сайт", url="https://narochguesthouse.by/")
        contacts="""Максим:
Телефон: +375293600588
Telegram: @Stepenevo

Юлия:
Телефон: +375293200588
Telegram: @YulRoz

Почта:
Email: naroch17guesthouse@gmail.com

Вы можете заполнить форму для обратной связи на сайте
        """
       
        markup.add(narochguesthouse_by)
        bot.send_message(message.chat.id, contacts, reply_markup=markup)
        

    @bot.message_handler(commands=["services"]) # Услуги
    def serv(message):
        markup = types.InlineKeyboardMarkup()
        narochguesthouse_by = types.InlineKeyboardButton("Ознакомьтесь с услугами на сайте", url="https://narochguesthouse.by/booking/")
        services = """Услуги:

Бесплатная частная охраняемая парковка
Wi-Fi, предоставляется в общественных зонах бесплатно
Трансфер (оплачивается отдельно)
Баня (оплачивается отдельно)
Размещение домашних животных допускается
Место для пикника
Принадлежности для барбекю
Шезлонги
Полотенца для бассейна/пляжа
Места для курения (курение в номерах запрещено)
Отопление
Семейные номера
Номера для некурящих
Бадминтон
Настольные игры
Велосипеды (оплачивается отдельно)
Лодка (оплачивается отдельно)
        """
        markup.add(narochguesthouse_by)
        bot.send_message(message.chat.id, services, reply_markup=markup)

    @bot.message_handler(commands=["prices"]) # Цены
    def pr(message):
        markup = types.InlineKeyboardMarkup()
        narochguesthouse_by = types.InlineKeyboardButton("Ознакомьтесь с ценами на сайте", url="https://narochguesthouse.by/booking/")
        price = """Цены (указаны за 1-го человека):

Новогодние праздники, июнь-август:
50 бел руб (Дом с удобствами)
40 бел руб (Дом без удобств: кухня, санузел на улице)

Межсезонье:
40 бел руб (Дом с удобствами)
30 бел руб (Дом без удобств)

Мы можем разместить до 10 человек(максимально)
        """
        markup.add(narochguesthouse_by)
        bot.send_message(message.chat.id, price, reply_markup=markup)

    @bot.message_handler(commands=["link"]) # Сайты
    def link(message):
        markup = types.InlineKeyboardMarkup() # Кнопки сайтов
        narochguesthouse_by = types.InlineKeyboardButton("Наш сайт", url="https://narochguesthouse.by/")
        booking = types.InlineKeyboardButton("Booking", url="https://www.booking.com/hotel/by/naroch-guest-house.ru.html")
        kufar = types.InlineKeyboardButton("Kufar", url="https://re.kufar.by/vi/minskaya-oblast/snyat/dom-na-sutki/151857498")
        vetliva = types.InlineKeyboardButton ("Vetliva",url="https://vetliva.ru/tourism/where-to-stay/gostevye-domiki-naroch/index.php?currency=BYN&booking%5Bid%5D%5B0%5D=18597")
        flatby = types.InlineKeyboardButton("Flatby", url="https://flatby.by/kottedzh-272")
        markup.add(narochguesthouse_by,booking,kufar,vetliva,flatby)
        bot.send_message(message.chat.id,"Сайты: ", reply_markup=markup)

    @bot.message_handler(commands=["geolocation"]) # Геолокация
    def geo(message):
        bot.send_message(message.chat.id, "[Геолокация](https://www.google.com/maps/place/Naroch+Guest+House/@54.8826102,26.6765867,15z/data=!4m8!3m7!1s0x0:0xc4691d054bcc9d8c!5m2!4m1!1i2!8m2!3d54.8826102!4d26.6765867)"
        , parse_mode='Markdown')

    @bot.message_handler(commands=["calendar"]) # Календарь бронирования
    def cl(message):
        bot.send_message(message.chat.id,"[Календарь](https://narochguesthouse.by/calendar)", parse_mode='Markdown')

    @bot.message_handler(commands=["photo"]) # Фото
    def photo_house(message):
        markup = types.InlineKeyboardMarkup()
        narochguesthouse_by = types.InlineKeyboardButton("Галерея", url="https://narochguesthouse.by/gallery/")
        markup.add(narochguesthouse_by)
        photo_1 = open("./PhotoNarochBot/1.jpg", 'rb')
        photo_2 = open("./PhotoNarochBot/2.jpg", 'rb')
        photo_3 = open("./PhotoNarochBot/3.jpg", 'rb')
        photo_4 = open("./PhotoNarochBot/4.jpg", 'rb')
        photo_5 = open("./PhotoNarochBot/5.jpg", 'rb')
        photo_6 = open("./PhotoNarochBot/6.jpg", 'rb')
        photo_7 = open("./PhotoNarochBot/7.jpg", 'rb')
        photo_8 = open("./PhotoNarochBot/8.jpg", 'rb')
        photo_9 = open("./PhotoNarochBot/9.jpg", 'rb')
        photo_10 = open("./PhotoNarochBot/10.jpg", 'rb')
        bot.send_photo(message.chat.id, photo_1)
        bot.send_photo(message.chat.id, photo_2)
        bot.send_photo(message.chat.id, photo_3)
        bot.send_photo(message.chat.id, photo_4)
        bot.send_photo(message.chat.id, photo_5)
        bot.send_photo(message.chat.id, photo_6)
        bot.send_photo(message.chat.id, photo_7)
        bot.send_photo(message.chat.id, photo_8)
        bot.send_photo(message.chat.id, photo_9)
        bot.send_photo(message.chat.id, photo_10)
        bot.send_message(message.chat.id,"Больше фото на сайте", reply_markup=markup)
        photo_1,photo_2,photo_3,photo_4,photo_5,photo_6,photo_7,photo_8,photo_9,photo_10.close()

    @bot.message_handler(content_types=["text"])  # Обработчик команд
    def get_user_text(message):
        markup = types.InlineKeyboardMarkup()
        narochguesthouse_by = types.InlineKeyboardButton("Посетите наш сайт", url="https://narochguesthouse.by/gallery/")
        markup.add(narochguesthouse_by)
        description = """Команды:
        Запуск бота - /start
        Контактная информация - /contacts
        Предоставляемые услуги - /services
        Цены - /prices
        Геолокация - /geolocation
        Немного фоточек - /photo
        Ссылки на сайты для бронирования - /link
        Календарь бронирования - /calendar
        """
        if message.text == "Помощь" or message.text == "помощь" or message.text == "Help":
            bot.send_message(message.chat.id, description, reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Я тебя не понимаю")


    bot.polling(none_stop=True)

if __name__ == "__main__":
    telegram_bot(token)
