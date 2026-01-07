import telebot

# Замените 'YOUR_BOT_TOKEN' на ваш токен бота
TOKEN = '8565680729:AAEOEa1Yg9JtCYyytrFiUf5MJfgoT1HVQ7I'
OWNER_CHAT_ID = '970637789'  # Замените на ваш chat_id
GROUP_LINK = 'https://t.me/+M9UVweGkIaFlNDUy'  # Ссылка на закрытую группу

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Пожалуйста, укажите свое ФИО.")
    bot.register_next_step_handler(message, get_full_name)

def get_full_name(message):
    full_name = message.text
    bot.send_message(message.chat.id, "Спасибо! Теперь укажите ваш адрес.")
    bot.register_next_step_handler(message, get_address, full_name)

def get_address(message, full_name):
    address = message.text

    # Отправка данных владельцу бота
    data = f"ФИО: {full_name}\nАдрес: {address}"
    bot.send_message(OWNER_CHAT_ID, data)

    # Отправка ссылки на закрытую группу пользователю
    bot.send_message(message.chat.id, f"Спасибо! Ваша информация была отправлена. Вот ссылка на закрытую группу: {GROUP_LINK}")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
