from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import os
import telegram
import logging
from dotenv import load_dotenv
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

from Functions import aux_functions

load_dotenv()

token = os.environ['TELEGRAM_BOT_APIKEY']
bot = telegram.Bot(token=token)

updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Eu sou a SimpatiBot, manda o luxo aí")


start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)



def check_messages(update, context): ##Here
    checked_message = aux_functions.is_link(update.message.text)
    if checked_message[0]:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=checked_message[1])


check_handler = MessageHandler(
    Filters.text & (~Filters.command), check_messages)
dispatcher.add_handler(check_handler)


#Funcao teste de comandos do tipo /comando
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

#Funcao teste com comando /dot que reenvia o texto com um ponto final
def dot(update, context):
    text_dot = ' '.join(context.args) + '.'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_dot)


dot_handler = CommandHandler('dot', dot)
dispatcher.add_handler(dot_handler)


#Funcao teste de inlineQuery
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


if __name__ == '__main__':
    updater.start_polling()
