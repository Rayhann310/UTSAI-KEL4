# mengimport package pyTelegramBotAPI
import telebot

# inisialisasi Token Bot Kita
bot = telebot.TeleBot('6032186596:AAHZSjSz06OJ_fRIWxms9g_x2nBYCsGZkSk')

# Menghandle Pesan /start
@bot.message_handler(commands=['tanya'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Halo bro, ada apa?')

while True:
    try:
        bot.polling()
    except:
        pass