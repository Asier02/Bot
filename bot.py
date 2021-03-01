# -*- coding: utf-8 -*-
 
import telebot
from telebot import types 
import time
import random
 
TOKEN = ''
GRUPO = 
 
bot = telebot.TeleBot(TOKEN) 

commands = {
    'start'       : 'Comienza a usar el bot',
    'ayuda'       : 'Proporciona información sobre los comandos',
    'cat'         : 'Envía la foto de un precioso michi',
    'pole'        : 'Envía un gift para hacer saber al grupo que has hecho pole'
}
 
def listener(messages): 
    for m in messages: 
        cid = m.chat.id 
        if cid > 0:
            mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text 
        else:
            mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text 
        f = open( 'log.txt', 'a') 
        f.write(mensaje + "\n") 
        f.close()
        print (mensaje)

bot.set_update_listener(listener)

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  
        knownUsers.append(cid)  
        userStep[cid] = 0 
        bot.send_message(cid, "Hola!, espera un momento que analizo...")
        bot.send_message(cid, "Análisis completo, bienvenido/a")
        command_help(m)
    else:
        bot.send_message(cid, "Bienvenido de nuevo")

@bot.message_handler(commands=['ayuda'])
def command_help(m):
    cid = m.chat.id
    help_text = "Los siguentes comandos están disponibles: \n"
    for key in commands:  
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)

@bot.message_handler(commands=['cat'])
def command_cat(m):
    cid = m.chat.id
    bot.send_sticker(cid, open(str(random.randint(1, n)) + ".jpg" or ".webp", "rb"))

@bot.message_handler(commands=['pole'])
def pole(m):
    cid = m.chat.id
    bot.send_sticker(cid, open("Pole.webp","rb"))

@bot.message_handler(func=lambda message: message.text == "Hola")
def command_text_hola(m):
    time.sleep(1)
    bot.send_message(m.chat.id, "Hola a ti tambien")

@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    if not is_api_group(message.chat.id):
        return
    name = message.new_chat_participant.first_name
    if hasattr(message.new_chat_participant, 'last_name') and message.new_chat_participant.last_name is not None:
        name += u" {}".format(message.new_chat_participant.last_name)
    if hasattr(message.new_chat_participant, 'username') and message.new_chat_participant.username is not None:
        name += u" (@{})".format(message.new_chat_participant.username)
    bot.reply_to(message, text_messages['Bienvenido'].format(name=name))

bot.polling()
