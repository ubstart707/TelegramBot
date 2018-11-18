import telebot

import tokenn
from time import gmtime, strftime


bot = telebot.TeleBot(tokenn.token2)


bot.send_message(379019794, "test")

# part of Salah times
#################################################################
#
#
from bs4 import BeautifulSoup  #
import requests  #

#
#
url = 'https://www.islom.uz/'  #
r = requests.get(url)  #
soup = BeautifulSoup(r.text, 'html.parser')  #
path = ''  #
#
#
namaazTimes = soup.select('div.p_clock')  #
namaazTimes = [namaazTime.text for namaazTime in namaazTimes]  #
#
#
del namaazTimes[1]  #
#
Bomdot = namaazTimes[0]  #
Peshin = namaazTimes[1]  #
Asr = namaazTimes[2]  #
Shom = namaazTimes[3]  #
Xufton = namaazTimes[4]  #
#
Namoz_vaqtlari = (
    " Bomdot vaqti: {0}\n Peshin vaqti: {1}\n Asr vaqti: {2}\n Shom vaqti: {3}\n Xufton vaqti: {4}".format(Bomdot,
                                                                                                           Peshin, Asr,
                                                                                                           Shom,
                                                                                                           Xufton))


bomdot_vaqti = ("Bomdot vaqti: {0}".format(Bomdot))
peshin_vaqti = ("Peshin vaqti: {0}".format(Peshin))
asr_vaqti = ("Asr vaqti: {0}".format(Asr))
shom_vaqti = ("Shom vaqti: {0}".format(Shom))
xufton_vaqti = ("Xufton vaqti: {0}".format(Xufton))

#
#
print(Namoz_vaqtlari)  #

with open("chat_id.txt", "a") as file:
    file=file
f = open("chat_id.txt", "a")
#################################################################

@bot.message_handler(commands=['start'])
def heandle_text(message):
    bot.send_message(message.chat.id, """ Asaalomu aleykum! bu bot sizga Toshkent namoz vaqtlarini bilishda yordam beradi
    Assalomu aleykum! eto bot pomojet vam chtobi uznat vremya namaz  Tashkenta,
    Assalomu aleykum!This bot help to you know about Tashkent's Salah time""")
    # if message.chat.id in open('chat_id.txt',"r"):
    #     print("user has")
    # else:
    #     f.write(str(message.chat.id))
    f = open("chat_id.txt", "a+")
    s = str(message.chat.id)+"\n"
    f.write(s)
    print(message.chat.id,message.text)

@bot.message_handler(commands=['bomdot'])
def heandle_text(message):
    bot.send_message(message.chat.id, bomdot_vaqti)
    print(message.chat.id,message.text)


@bot.message_handler(commands=['peshin'])
def heandle_text(message):
    bot.send_message(message.chat.id, peshin_vaqti)
    print(message.chat.id,message.text)

@bot.message_handler(commands=['asr'])
def heandle_text(message):
    bot.send_message(message.chat.id, asr_vaqti)
    print(message.chat.id,message.text)


@bot.message_handler(commands=['shom'])
def heandle_text(message):
    bot.send_message(message.chat.id, shom_vaqti)
    print(message.chat.id,message.text)


@bot.message_handler(commands=['xufton'])
def heandle_text(message):
    bot.send_message(message.chat.id, xufton_vaqti)
    print(message.chat.id,message.text)


@bot.message_handler(content_types=["text"])
def heandle_text(message):

    if message.text == "bomdot":
        bot.send_message(message.chat.id, bomdot_vaqti)
        print(message.chat.id,message.text)

    elif message.text == "peshin":
        bot.send_message(message.chat.id, peshin_vaqti)
        print(message.chat.id,message.text)

    elif message.text == "asr":
        bot.send_message(message.chat.id, asr_vaqti)
        print(message.chat.id,message.text)

    elif message.text == "shom":
        bot.send_message(message.chat.id, shom_vaqti)
        print(message.chat.id,message.text)

    elif message.text == "xufton":
        bot.send_message(message.chat.id, xufton_vaqti)
        print(message.chat.id,message.text)
    else:
        bot.send_message(message.chat.id, Namoz_vaqtlari)
        print(message.chat.id,message.text)



time = strftime("%X")
time_hour = time[0] + time[1]
time_minut = time[3] + time[4]
clock = time_hour + ":" + time_minut

if clock == Bomdot:
    bot.send_message(379019794, bomdot_vaqti)

if clock == Peshin:
    bot.send_message(379019794, peshin_vaqti)

if clock == Asr:
    bot.send_message(379019794, asr_vaqti)

if clock == Shom:
    bot.send_message(379019794, shom_vaqti)

elif clock == Xufton:
    bot.send_message(379019794, xufton_vaqti)
if clock == "23:27":
    bot.send_message(379019794, xufton_vaqti)

if isinstance(update, Update) and update.inline_query:
           if self.pattern:
               if update.inline_query.query:
                   match = re.match(self.pattern, update.inline_query.query)
                   return bool(match)
           else:
               return True

bot.polling()