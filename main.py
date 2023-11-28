import telebot
bot = telebot.TeleBot( '6445755957:AAFr1szB5vTGF_bNxOWggwCjjSyHcbsg0UQ' )

@bot.message_handler ( commands = [ 'start' ])
def main(message):
    bot.send_message(message.chat.id, 'Привет, нужна цитата?', parse_mode='Markdown')

@bot.message_handler ( commands = ['citata_stekhem'])
def main(message):
    bot.send_message(message.chat.id, 'Только пепел знает, что значит гореть до тла', parse_mode='Markdown')

@bot.message_handler ( commands = [ 'citata_volka' ])
def main(message):
    bot.send_message(message.chat.id, 'Если говорят за твоей спиной, значит ты впереди.', parse_mode='Markdown')

@bot.message_handler ( commands = [ 'citata_fun' ])
def main(message):
    bot.send_message(message.chat.id, 'Запомни...\nзабудь.', parse_mode='Markdown')
bot.infinity_polling()