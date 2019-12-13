import os

from telebot.types import InlineKeyboardButton

class Config:    
    @staticmethod
    def get_mode():
        MODE = os.environ.get('MODE')
        if MODE != "prod":
        	MODE = "debug"
        return MODE

    @staticmethod
    def get_token():
    	BOT_TOKEN = os.environ.get('BOT_TOKEN')
    	if BOT_TOKEN is None:
    		with open("bot.token") as f:
    			BOT_TOKEN = f.readline()
    	return BOT_TOKEN

    @staticmethod
    def get_url():
    	URL = os.environ.get('HEROKU_URL')
    	return URL

def autosending_text(bot, message):
    first_name = bot.get_chat(message.chat.id).first_name
    text = "Hello, {0}".format(first_name)
    return text