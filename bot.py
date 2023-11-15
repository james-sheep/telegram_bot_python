import os
import telebot
from telebot import types
import urllib
import json


SECRETKEY= "dhheheudsuapropriakey"

bot = telebot.TeleBot(SECRETKEY, parse_mode = None)


@bot.message_handler(commands=['Curiosidades'])
def send_start_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('/people')
    itembtnb = types.KeyboardButton('/voltar')
    markup.row(itembtna, itembtnb)
    bot.reply_to(message, " Quer saber quem está no espaço neste exato momento?'\n"
                          "Envie o comando /people para saber.", reply_markup=markup)


@bot.message_handler(commands=['command1', 'Ola', 'Bom dia ', 'Boa tarde', 'voltar' ])
def send_start_message(message):
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('/Solicitações')
    itembtnv = types.KeyboardButton('/Agendamentos')
    itembtnd = types.KeyboardButton('/Curiosidades')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnd)
    bot.reply_to(message, "Olá, eu sou o bot , ainda estou em desenvolvimento mas pretendo administrar todas a mensagens do meu chefinho", reply_markup=markup)
    

@bot.message_handler(commands=['informação', 'Solicitações','command2'])
def send_start_message(message):
    bot.reply_to(message, "Em se tratando de informações ou solicitações processuais, não esqueça de mencionar o número do 1doc ou do processo judicial")
    
    @bot.message_handler(func = lambda  message : True)
    def captura_resposta(message):
        bot.reply_to(message, "Solicitação recebida com sucesso")
        
      

@bot.message_handler(commands=['Reunião', 'Agendamentos','command3', 'reunião'])
def send_start_message(message):
    bot.reply_to(message, "Informe resumidamente o assunto da reunião e a melhor data para você. \n Assim que confirmarmos a Agenda entraremos em contato. \n Obrigado. ")
    
    @bot.message_handler(func = lambda  message : True)
    def captura_resposta(message):
        bot.reply_to(message, "Solicitação recebida com sucesso")
        #adicionar funçao


@bot.message_handler(commands=['people'])
def send_people(message):
    bot.reply_to(message, get_reply_message())


def get_reply_message():
    n_people, people = get_people()
    message = "Existem " \
              + str(n_people) + \
              " pessoas no espaço neste momento, são elas: \n\n"
    for person in people:
        message += person["name"] + \
                   " na espaçonave " + person["craft"] + "\n\n"

    return message


def get_people():
    req = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(req)

    obj = json.loads(response.read())

    return obj["number"], obj["people"]


bot.polling()
