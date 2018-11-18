import telebot
import tokenn

bot = telebot.TeleBot(tokenn.token)

bot.send_message(449967898, "test")
#
# upd = bot.get_updates()
#
#
# last_upd = upd[-1]
#
# message_from_user = last_upd.message
#
# print(message_from_user)

print(bot.get_me())

a = 42
b = "qwerty"
print(type(a), type(b))

def log(message, answer):
    print("\n --------")


    from datetime import datetime
    print(datetime.now())
    print("Message from [0] [1] . (id = [2]) \n Text =[3]".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))

    print(answer)

    bot.send_message(message.chat.id)




@bot.message_handler(commands=['help'])
def heandle_text(message):
    bot.send_message(message.chat.id, """Ulug'bek test boti urganish uchun.
    lekin buni qilish uchun 3 hafta vaqt ketdii
    :(""")





@bot.message_handler(content_types=["text"])
def heandle_text(message):
    answer = "You dont know how to play this game"

    if message.text == "a":
        answer = "B"
        log(message, answer)
        bot.send_message(message.chat.id, answer)

    elif message.text == "б":
        answer = "B"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)

bot.polling(none_stop=True, interval=0)