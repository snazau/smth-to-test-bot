import os

from telebot.types import InlineKeyboardButton


class Config:
    BOT_TOKEN = os.environ['BOT_TOKEN']
    MODE = os.environ['MODE']


def autosending_text(bot, message):
    first_name = bot.get_chat(message.chat.id).first_name
    text = """Hello, {0}""".format(first_name)
    return text

