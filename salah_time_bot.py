import requests
import json
import logging

from telegram.ext import Updater
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CommandHandler

updater = Updater(token='635554915:AAFVe6nAU66LYVHSZVFGakqiA2rGxwxu0tc')# @salagtime_bot telegram bots ip
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)




#part of Salah times
#################################################################
                                                                #
																#
from bs4 import BeautifulSoup									#
import requests													#
																#
																#	
url = 'https://www.islom.uz/'									#
r = requests.get(url)											#
soup = BeautifulSoup(r.text, 'html.parser')						#
path = ''														#
																#
																#
namaazTimes = soup.select('div.p_clock')						#
namaazTimes = [namaazTime.text for namaazTime in namaazTimes]	#
																#
																#
del namaazTimes[1]												#
																#
Bomdot = namaazTimes[0]											#
Peshin = namaazTimes[1]											#
Asr = namaazTimes[2]											#
Shom = namaazTimes[3]											#
Xufton = namaazTimes[4]											#
																#
Namoz_vaqtlari = (" Bomdot vaqti: {0}\n Peshin vaqti: {1}\n Asr vaqti: {2}\n Shom vaqti: {3}\n Xufton vaqti: {4}".format(Bomdot, Peshin, Asr, Shom, Xufton))
																#
																#
print(Namoz_vaqtlari)                               			#
																#
#################################################################
import time
dt = list(time.localtime())
hour = dt[3]
minute = dt[4]
if hour == 1 and minute == 5:
    print("alarm 01:48s")#

#part of salahtime bot
#############################################################################################################################################################
chat_id1=''
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Asaalomu aleykum! bu bot sizga Toshkent namoz vaqtlarini bilishda yordam beradi \nAssalomu aleykum! eto bot pomojet vam chtobi uznat vremya namaz  Tashkenta\nAssalomu aleykum!This bot help to you know about Tashkent's Salah time")
	# bot.send_message(chat_id=update.message.chat_id, text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.', parse_mode=telegram.ParseMode.HTML )
	

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def starts(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Asaalomu aleykum! bu bot sizga Toshkent namoz vaqtlarini bilishda yordam beradi \nAssalomu aleykum! eto bot pomojet vam chtobi uznat vremya namaz  Tashkenta\nAssalomu aleykum!This bot help to you know about Tashkent's Salah time")

if __name__ == "__main__":
    	starts
  
#-->Bomdot<--
def bomdot(bot, update):    
    bot.send_message(chat_id=update.message.chat_id, text=Bomdot)
bomdot_handler = CommandHandler('bomdot', bomdot)
dispatcher.add_handler(bomdot_handler)


#-->Peshin<--
def peshin(bot, update):    
    bot.send_message(chat_id=update.message.chat_id, text=Peshin)
peshin_handler = CommandHandler('peshin', peshin)
dispatcher.add_handler(peshin_handler)

def sendSimpleText(chat_id, update, bot):
    bot.send_essage(chat_id=update.message.chat_id,text='faez')
#-->Asr<--
def asr(bot, update):    
    bot.send_message(chat_id=update.message.chat_id, text=Asr)
asr_handler = CommandHandler('asr', asr)
dispatcher.add_handler(asr_handler)

#--><--
def shom(bot, update):    
    bot.send_message(chat_id=update.message.chat_id, text=Shom)
shom_handler = CommandHandler('shom', shom)
dispatcher.add_handler(shom_handler)

#-->XUFTON<--
def xufton(bot, update):    
    bot.send_message(chat_id=update.message.chat_id, text=Xufton)
xufton_handler = CommandHandler('xufton', xufton)
dispatcher.add_handler(xufton_handler)

# bot.send_message(chat_id=  text="I'm sorry Dave I'm afraid I can't do that.")
# def test(bot, update):
#     update.send_message(chat_id='@python_test_channel', text='this is a test')

# def main():
#     # Create the EventHandler and pass it your bot's token.
#     updater = Updater("457160310:AAFlxrH2uAaOMGrgO0suOXFM2gVKywsUL0E")
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("test", test))

#     dp.add_error_handler(error)

#     updater.start_polling()

#     updater.idle()


# if __name__ == '__main__':
#     main()

updater.start_polling()
