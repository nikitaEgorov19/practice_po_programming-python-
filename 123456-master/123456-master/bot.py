import datetime
from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types
from fake_useragent import UserAgent
import dota2rerre

bot = telebot.TeleBot("1067004343:AAGZyE6geFbxe-4cGuvWNeW79m43Z9D_wWw")

inf = dota2rerre.get_matches()

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
a = types.KeyboardButton('Dota#2‼')
e = types.KeyboardButton('👾Не нажимать👾')
markup_menu.add(a, e)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Это не то, бро=(. Лучше напишу что нибудь', reply_markup=markup_menu)


@bot.message_handler(content_types=['text'])
def echo_digits(message):
    chat_id = message.chat.id
    if message.text == 'Dota#2‼':
        for i in range(len(inf)):
            bot.send_message(chat_id, '{}  {}  {}  {}  {}'.format(inf[i][0], inf[i][1], inf[i][2], inf[i][3],inf[i][4]))


bot.polling()

