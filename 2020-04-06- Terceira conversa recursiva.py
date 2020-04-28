#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:23:01 2020

@author: beatrizsilva
"""

import logging

from telegram import (InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup,
                      ReplyKeyboardRemove, MessageEntity)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)

import Switch_escolha

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Estados do primeiro nivel
SELECIONANDO_AREA, ADD_OPERADOR, ADD_SOFTWARE, ADD_EQUIPAMENTO = map(chr, range(4))
#Estados do segundo passo do nivel 1
(SELECIONA_OPERADOR, SELECIONA_SOFTWARE, SELECIONA_EQUIPAMENTO, AJUDA_OPERACOES,
 VOLTA_COMECO, ESCOLHE_SUBAREA, AJUDA, ENCAMINHA_AJUDA)= map(chr, range(4,12))

#Estados do segundo nivel
INPUT_PN, SALVA_INPUT, SELECIONA_QUE, SELECIONA_BO_SOFT = map(chr, range(12,16))

#Estados de software
SAURON, HARPIA, TUPAN, GEOCAM, REDIRECIONA_SOFTWARE = map(chr, range(16, 21))

#Estados de redirecionamento software
(STREAMING, TUTORIAL_COMPLETO, REPORTA_ERRO, DICIONARIO_TUTORIAIS, CREDENCIAIS,
 LINK, DEBUG, ADD_TUTORIAL) = map(chr, range(21, 29))

# Meta states
STOPPING, SHOWING = map(chr, range(29, 31))

# Shortcut for ConversationHandler.END
END = ConversationHandler.END

document = open('Procedimento_de_Purge.pdf', 'rb')

def start(update, context):
    user = update.message.from_user
    
    reply_keyboard = [['Operacao', 'Software', 'Equipamento', 'Encaminhar registro']]
 
    update.message.reply_text(
        'Olá, eu sou o assistente de operação da ALTAVE. Estou aqui para te'\
        ' ajudar com o seu chamado. '\
        'Por favor, escolha sobre o que você deseja reportar.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    logger.info("%s %s abriu chamado", user.first_name, user.last_name)
    return SELECIONANDO_AREA

def selecionando_area(update, context):
    user = update.message.from_user
    area = update.message.text
     
    if area == 'Operacao':
         
        user = update.message.from_user
        reply_keyboard = [['Mudar responsavel pela operacao'],
        ['Informar troca de operador'],
        ['Acidente, emergencia ou mal estar']]
        
        update.message.reply_text(
                'Selecione uma das ações',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

        logger.info("%s reporta sobre %s", user.first_name, update.message.text)

        return SELECIONA_OPERADOR
    
    elif area == 'Software':

        user = update.message.from_user
        reply_keyboard = [['Harpia', 'Tupan', 
                       'Sauron', 'Geocam']]
    
        update.message.reply_text(
                'Selecione entre um dos softwares desenvolvidos pela ALTAVE',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

        logger.info("%s reporta sobre %s", user.first_name, update.message.text)
        user = update.message.from_user
    
        return SELECIONA_SOFTWARE
    
    elif area == 'Equipamento':
        user = update.message.from_user
        reply_keyboard = [['Balao', 'Guincho', 'Gondola'],
                ['Cabo de ancoragem', 'Caixa de dados'],
                ['Caixa do guincho', 'Berço de solo', 'Berço da pizza/picape']]
    
        logger.info("%s reporta sobre %s", user.first_name, update.message.text)
        update.message.reply_text(
                'Selecione entre um dos hardware desenvolvidos pela ALTAVE',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
        return SELECIONA_EQUIPAMENTO
         
        
    else:
        user = update.message.from_user
        reply_keyboard = [['Tenho certeza, chama o Inaldo.'],
                ['Voltar']]
     
        update.message.reply_text(
            'Tem certeza?',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        
        
        return AJUDA
        
    return ESCOLHE_SUBAREA

def digita_ajuda(update, context):
    escolha = update.message.text
    user = update.message.from_user
    
    if escolha == 'Tenho certeza, chama o Inaldo.':
        logger.info("%s %s está pedindo ajuda para o Inaldo: %s", user.first_name, user.last_name, update.message.text)
        update.message.reply_text('Entendi. O que você quer falar?')
 
        return ENCAMINHA_AJUDA

    else:
        user = update.message.from_user
        reply_keyboard = [['/recomeca', '/cancela']]
     
        update.message.reply_text(
            'Beleza!',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        logger.info("%s %s cancelou", user.first_name, user.last_name)
            
        return VOLTA_COMECO
 
def encaminha_ajuda(update, context):

    user = update.message.from_user
    logger.info("%s %s está pedindo ajuda para o Inaldo: %s", user.first_name, user.last_name, update.message.text)
    
    
    context.bot.sendMessage('582892178', 'Olá Inaldo, sua equipe precisa falar com você!',
                        parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                        reply_to_message_id=None, reply_markup=None, timeout=None)
    
    context.bot.forwardMessage(chat_id='582892178', from_chat_id=update.message.chat_id,
                                message_id=update.message.message_id)
    
    
    return AJUDA_OPERACOES

################################
# Encaminha problemas de software, supõe que os problemas são todos da mesma grande natureza e salva as entradas anteriores
# Chamar o estado SELECIONA_SOFTWARE para esse estado

def seleciona_software(update, context):
    
    software = update.message.text

    if software == 'Sauron':
        user = update.message.from_user
        reply_keyboard = [['Acesso','Streaming','Tutorial completo', 'Acusar Erro']]
        
        update.message.reply_text(
            'Ajuda com o que?',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

        return SAURON


    elif software == 'Harpia':
        user = update.message.from_user
        reply_keyboard = [['Acesso','Streaming','Tutorial completo','Credenciais','Link de acesso']]

        update.message.reply_text(
            'Ajuda com o que?',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

        return HARPIA
        

    elif software == 'Tupan':
        user = update.message.from_user
        reply_keyboard = [['Acesso','Link de acesso','Acusar Erro']]

        update.message.reply_text(
            'Ajuda com o que?',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

        return TUPAN
        

    elif software == 'Geocam':
        user = update.message.from_user
        reply_keyboard = [['ERRO 1','ERRO 2','Tutorial completo']]

        update.message.reply_text(
            'Ajuda com o que?',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

        return GEOCAM

    return REDIRECIONA_SOFTWARE


################################




def stop(update, context):
    """End Conversation by command."""
    update.message.reply_text('Ta bom, tchau.')

    return END


def end(update, context):
    """End conversation from InlineKeyboardButton."""
    text = 'Te vejo por ai!'
    update.callback_query.edit_message_text(text=text)

    return END
 
 
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
 

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    TOKEN = "863859400:AAHePje4fFREUqhThSd3xhOMqMSNtDkCroY"
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
   
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
 
        states={
            SELECIONANDO_AREA: [MessageHandler(Filters.regex('^(Operacao|Software|Equipamento|Encaminhar registro)$'), selecionando_area),
                                CommandHandler('start', start)],
            AJUDA: [MessageHandler(Filters.regex('^Tenho certeza, chama o Inaldo.|Voltar$'), digita_ajuda)],
            ENCAMINHA_AJUDA: [MessageHandler(Filters.text, encaminha_ajuda)],
            SELECIONA_SOFTWARE: [MessageHandler(Filters.regex('^(Harpia|Tupan|Sauron|Geocam$)$'), seleciona_software)],
            REDIRECIONA_SOFTWARE: [MessageHandler(Filters.regex('^(Acesso|Streaming|Tutorial Completo|Acusar Erro|Outros tutoriais|Credenciais|Link de acesso|Debug|Adicionar_tutorial$)$'), redireciona_software)],
            #VOLTA_COMECO: [CallbackQueryHandler(end, pattern='^' + str(END) + '$'),
                           #CallbackQueryHandler(start, pattern='^' + str(END) + '$')],
        },
 
        fallbacks=[CommandHandler('cancela', stop)]
    )
 
    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
 
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
 
 
if __name__ == '__main__':
    main()