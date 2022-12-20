import telebot
import random
from flask import Flask, request
import os


server = Flask(__name__)
bot = telebot.TeleBot('5879551227:AAG2HSXqGAS592uAdkhTZqEFuiLoUXIEjXw')

subjects = ["#алгебра", "#русский", "#литра", "#англ", "#история", "#башяз", "#башлит", "#астрономия"]
answers = ["хорош", "лучший", "спс"]



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "салам")


@bot.message_handler(content_types=['text', 'photo'],
                     func=lambda message: message.chat.id != -820699648)
def forward(message):
    #print(message.caption.split())
    if any([i for i in message.text.split() if i in subjects or i[:-2] in subjects]):
        bot.send_message(message.chat.id, random.choice(answers))
        bot.forward_message(-820699648, from_chat_id=message.chat.id, message_id=message.message_id)
    if any([i for i in message.caption.split() if i in subjects or i[:-2] in subjects]):
        bot.send_message(message.chat.id, random.choice(answers))
        bot.forward_message(-820699648, from_chat_id=message.chat.id, message_id=message.message_id)

@server.route('/' + '5879551227:AAG2HSXqGAS592uAdkhTZqEFuiLoUXIEjXw', methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://zazaza-bot.herokuapp.com/' + '5879551227:AAG2HSXqGAS592uAdkhTZqEFuiLoUXIEjXw')
    return "!", 200

if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
