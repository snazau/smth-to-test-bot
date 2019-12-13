import telebot
import logging
from config import *

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

bot = telebot.TeleBot(Config.BOT_TOKEN)

@bot.message_handler(
    content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location',
                   'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo',
                   'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created',
                   'migrate_to_chat_id', 'migrate_from_chat_id',
                   'pinned_message'])
def sending_auto2(message):
    bot.send_message(chat_id=message.chat.id, text=autosending_text(bot, message), disable_web_page_preview=True)

if Config.MODE == "PROD":
	logger.debug("Config.MODE =", Config.MODE)

if __name__ == '__main__':
	logging.debug("Config.MODE", Config.MODE)
	bot.polling()  # Заставляет бота получать уведомления о новых сообщениях