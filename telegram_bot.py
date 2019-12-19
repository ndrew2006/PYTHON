import telebot

bot = telebot.TeleBot("1013942730:AAFQXXaz_KXhL5iJEKm1vWfs0_N-JVlQAXY")  # newpyweatherbot  newpyweather_bot

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)

bot.polling( none_stop=True )