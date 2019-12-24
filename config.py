import os
import dotenv

dotenv.load_dotenv()

class Config:
    MODE = os.getenv('MODE')
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    URL = os.getenv('HEROKU_URL')

def autosending_text(bot, message):
    first_name = bot.get_chat(message.chat.id).first_name
    text = "Hello kek, {0}".format(first_name)
    return text