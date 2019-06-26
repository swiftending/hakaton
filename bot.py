import telebot

token = "888041305:AAHtiYrbwdvfGLdIPwXH5xcUaimj0zbIFLQ"

# Обходим блокировку с помощью прокси
telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)
name = '';
surname = '';
@bot.message_handler(content_types=['text'])
def start(message):
    user = message.chat.id
    if message.text == '/reg':
        bot.send_message(user, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(user, 'Напиши /reg');

def get_name(message):
    user = message.chat.id
    global name;
    name = message.text;
    bot.send_message(user, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    user = message.chat.id
    global surname;
    surname = message.text;
    bot.send_message(user, ' Tебя зовут '+name+' '+surname+'?')
def dailinet(message):
    user = message.chat.id
    if text=="да":
        bot.send_message(user, 'Запомню : )')
    elif text=='нет':
        bot.send_message(user, 'переспрашиваю')
        start(message)
        get_name(message)
        get_surname(message)
        dailinet(message)
bot.polling(none_stop=True)
