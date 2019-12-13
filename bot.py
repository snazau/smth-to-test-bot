import telebot
import logging
from config import *

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

bot = telebot.TeleBot(Config.get_token())

@bot.message_handler(
    content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location',
                   'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo',
                   'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created',
                   'migrate_to_chat_id', 'migrate_from_chat_id',
                   'pinned_message'])
def answer_smth(message):
    bot.send_message(chat_id=message.chat.id, text=autosending_text(bot, message), disable_web_page_preview=True)

MODE = Config.get_mode()
TOKEN = Config.get_token()

if __name__ == '__main__':
	logging.info("Selected mode " + mode)
	if MODE == "debug":
		bot.polling()
		bot.remove_webhook()
	else:
		bot.set_webhook(Config.get_url() + TOKEN)