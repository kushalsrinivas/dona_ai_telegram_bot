import telebot
from utils import join_meet,getSerilisedText
api_key  = "6905027579:AAFEmVjm8Qi-S8O8Bq_ZHL821TYvz7p8IYg"
bot = telebot.TeleBot(api_key)

@bot.message_handler(commands=['commands'])
def commands(message):
    bot.send_message(message.chat.id, ("here is a list of commands" ),
                     parse_mode="Markdown")

@bot.message_handler(commands=['join'])
def join(message):
    link = (message.text.split()[1])
    deets = join_meet(link)
    while isinstance(deets , type(None)):
        print("waiting...")
        pass
    formatted_Text = f"\nAgenda:-\n{deets['agenda']}\nKey points :-\n{getSerilisedText(deets['KeyPoints']['data'])}\nTodo:-\n{getSerilisedText(deets['ActionPoints']['data'])}"
    print(formatted_Text)
    bot.send_message(message.chat.id, formatted_Text,
                     parse_mode="Markdown")


@bot.message_handler(commands=['table'])
def table(message):
    table = "<pre><pre>"
    bot.send_message(message.chat.id, (table),
                     parse_mode="HTML")
bot.polling()