import telebot
from telebot import types

my_bot = telebot.TeleBot('5126768290:AAFR-LNRj7uvdQUjbss1QR8wfIx4gAqq-bk')


@my_bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == 'Привет' or message.text == '/start':
        my_bot.send_message(message.from_user.id, 'Чтобы увидеть список команд введите /help')
    elif message.text == '/help':
        my_bot.send_message(message.from_user.id, 'Привет, вот список всех команд')
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # Список кнопок
        key_bestdeal = types.InlineKeyboardButton(text='В зависимости от центра города ', callback_data='beastdeal')
        keyboard.add(key_bestdeal)
        key_lowprice = types.InlineKeyboardButton(text='Самые низкие цены 10 отелей', callback_data='lowprice')
        keyboard.add(key_lowprice)
        key_highprice = types.InlineKeyboardButton(text='Самые дорогие цены 10 отелей', callback_data='highprice')
        keyboard.add(key_highprice)
        key_history = types.InlineKeyboardButton(text='История поиска', callback_data='history')
        keyboard.add(key_history)
        my_bot.send_message(message.from_user.id, text='Выберите нужную функцию', reply_markup=keyboard)
    else:
        my_bot.send_message(message.from_user.id, 'Я не понимаю вас. Напишите /help')


# Обработчик нажатий на кнопки
@my_bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 4 кнопок — вызываем функцию
    if call.data == 'bestdeal':
        my_bot.send_message(call.message.chat.id, 'Функция {} запущена. Отели по расстоянию от центра города'.
                            format(call.data))
        best_deal()
    elif call.data == 'lowprice':
        my_bot.send_message(call.message.chat.id, 'Функция {} запущена. Отели самые низкие по стоимости'.
                            format(call.data))
        low_price_hotels()
    elif call.data == 'highprice':
        my_bot.send_message(call.message.chat.id, 'Функция {} запущена. Отели самые дорогие по стоимости'.
                            format(call.data))
        high_price_hotels()
    elif call.data == 'history':
        my_bot.send_message(call.message.chat.id, 'Функция {} запущена. История запросов'.format(call.data))
        all_history()


# Запускаем постоянный опрос бота в Телеграме
my_bot.polling(none_stop=True, interval=0)
