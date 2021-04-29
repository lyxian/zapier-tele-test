from cryptography.fernet import Fernet
import requests
import telebot
import json
import os

def getToken():
    key = bytes(os.getenv('KEY'), 'utf-8')
    encrypted = bytes(os.getenv('API_KEY'), 'utf-8')
    return json.loads(Fernet(key).decrypt(encrypted))['api_key']

def createBot():
    TOKEN = getToken()

    bot = telebot.TeleBot(token=TOKEN)

    @bot.message_handler(commands=['hello'])
    def bot_hello(message):
        print(f'Reading message from {message.chat.id}...')
        text = 'Hello from BOT ☺♥☻♥'
        bot.send_message(message.chat.id, text, parse_mode=None)

    return bot

if __name__ == '__main__':
    bot = createBot()
    print(bot)