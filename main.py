
import telebot
from telebot import types

#5421006998:AAFJRc1SrbsehXr46FBk8-u4yk2DC0vb8aI

name = " "

bot = telebot.TeleBot("5421006998:AAFJRc1SrbsehXr46FBk8-u4yk2DC0vb8aI")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здравствуйте,давайте познакомимся,для этого нажмите /reg")

@bot . message_handler ( func = lambda m : True )
def echo_all( message ):
    if message.text == ("Я создатель"):
        bot.reply_to(message, "Очень приятно,но вы не Бог")
    elif message.text == ("/reg"):
        bot.send_message(message.from_user.id,"Как вас зовут?")
        bot.register_next_step_handler(message,reg_name)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id,"Очень приятно, меня зовут Tutti, я твой помошник в выборе музыки")

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="", repley_markkup=keyboard)
    keyboard.add(key_yes)

bot.infinity_polling()

#keyboard = types.InlineKeyboardMarkup()
#key_yes = types.InlineKeyboardButton(text= "/reg")
