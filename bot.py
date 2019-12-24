import telebot
import logging
from config import *
from flask import Flask, request

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

MODE = Config.MODE
TOKEN = Config.BOT_TOKEN
URL = Config.URL

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

# @bot.message_handler(
#     content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location',
#                    'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo',
#                    'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created',
#                    'migrate_to_chat_id', 'migrate_from_chat_id',
#                    'pinned_message'])
# def answer_smth(message):
#     bot.send_message(chat_id=message.chat.id, text=autosending_text(bot, message), disable_web_page_preview=True)

def sendMessage(message, text):
	bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['start'])
def send_info(message):
	text = (
	"<b>Welcome to the super bot 🤖!</b>\n"
	"Say Hello to the bot to get a reply from it!"
	)
	bot.send_message(message.chat.id, text, parse_mode='HTML')

@bot.message_handler(func=lambda msg: msg.text is not None)
def reply_to_message(message):
	if 'hello'in message.text.lower():
		sendMessage(message, 'Hello! How are you doing today?')
	else:
		phrase = ["Spam bot in da house", "Please", "type", "smth", "with", "word", "hello"]
		for word in phrase:
			sendMessage(message, word)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
	logging.info("KEKEKE @server.route('/' + TOKEN, methods=['POST'])")
	logging.info("type:" + type([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]))
	logging.info("smth" + [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
	return "!", 200

@server.route("/")
def webhook():
	logging.info('KEKEKE @server.route("/")')
	bot.remove_webhook()
	bot.set_webhook(url=URL + TOKEN)
	return "!", 200

if __name__ == '__main__':
	logging.info("Selected mode " + MODE)
	if MODE == "debug":
		bot.remove_webhook()
		bot.polling()
	else:
		server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
