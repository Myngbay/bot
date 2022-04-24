import requests
import telebot

my_bot = telebot.TeleBot('5126768290:AAFR-LNRj7uvdQUjbss1QR8wfIx4gAqq-bk')

url = "https://hotels4.p.rapidapi.com/properties/list"

querystring = {"destinationId": "1506246",
               "sortOrder": "PRICE", "locale": "en_US", "currency": "USD"}

headers = {
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com",
    "X-RapidAPI-Key": "181a0daa7bmshd1388bcd7434e9fp1d6f80jsn50f30b5122b2"
}

response = requests.request("GET", url, headers=headers, params=querystring)

all_data = response.json()

all_count_hotels = all_data['data']['body']['query']['searchResults']['totalCount']

@my_bot.message_handler(content_types=['text'])
def get_count_hotels(message):
    my_bot.send_message(message.from_user.id,
                        'В этом городе есть {} отелей. Сколько нужно вывести?\nМаксимальное количество 10'.
                        format(all_count_hotels))
    count = 0
    for index in all_data['data']:
        if count < 10:
            my_bot.send_message(message.from_user.id, 'Название отеля: {}'.format(
                                all_data['data']['body']['query']['searchResults']['results']['name']))
            my_bot.send_message(message.from_user.id, 'Адрес отеля: {}'.format(
                                all_data['data']['body']['query']['searchResults']
                                ['results']['address']['streetAddress']))
            my_bot.send_message(message.from_user.id, 'Расстояние от центра города: {}'.format(
                                all_data['data']['body']['query']['searchResults']['results']['landmarks']['distance']))


@my_bot.message_handler(content_types=['text'])
def best_deal():
    def get_message(message):
        my_bot.send_message(message.from_user.id, 'В каком городе искать отель? ')
        if message.text in all_data['data']['body']['header']:
            get_count_hotels()
        else:
            my_bot.send_message(message.from_user.id, 'Такого города в базе не нашлось!')

