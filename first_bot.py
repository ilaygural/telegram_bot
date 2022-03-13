import requests

TOKKEN = '5237824603:AAFfdut2L_pyuoiX4vovfjhyJgMnXovqL-I'  # КОНАСТАНТА С ТОКЕНОМ
API_link = 'https://api.telegram.org/bot' + TOKKEN  # ссылка на API
updates = requests.get(API_link + '/getUpdates')  # получение последних данных с API

# print(updates.json())  #расшифровка
message = updates.json()['result'][0]['message']  # берем последнее сообщение из расшифровки
# print(message)
chat_id = message['from']['id']
text_message = message['text']
# print(text_message)
send_message = requests.get(API_link + f'/sendMessage?chat_id={chat_id}&text=hi too you print -> {text_message}')  #Отправляем сообщение от бота
