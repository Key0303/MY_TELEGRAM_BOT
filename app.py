import telebot

# You can set parse_mode by default. HTML or MARKDOWN
bot = telebot.TeleBot(
    "", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá, Tudo bem ?")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Como posso ajudalo-lo ?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
