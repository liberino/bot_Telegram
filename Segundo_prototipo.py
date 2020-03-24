#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:21:46 2020

@author: beatrizsilva
"""


import logging

from telegram import (InlineKeyboardMarkup, InlineKeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Estados do primeiro nivel
SELECIONANDO_AREA, ADD_OPERADOR, ADD_SOFTWARE, ADD_EQUIPAMENTO = map(chr, range(4))
#Estados do segundo passo do nivel 1
SELECIONA_OPERADOR, SELECIONA_SOFTWARE, SELECIONA_EQUIPAMENTO = map(chr, range(4,7))

#Estados do terceiro nivel
INPUT_PN, SALVA_INPUT, SELECIONA_SAUDE, SELECIONA_BO_SOFT = map(chr, range(7,11))

# Constantes
(START_OVER, BRUNO, LEANDRO, VALDINIR, RAFAEL, BALAO, GUINCHO, GONDOLA, CDG, CEG,
 CABO_EM, HARPIA, TUPAN, SAURON, GEOCAM, FEATURES, CURRENT_FEATURE, RESPONSAVEL,
 OPERADOR, SAUDE, ACESSO, SENHA, LOCAL) = map(chr, range(11, 33))

# Meta states
STOPPING, SHOWING = map(chr, range(33, 35))

# Shortcut for ConversationHandler.END
END = ConversationHandler.END



# Primeiro nível da conversa. Escolha entre área de ajuda
def start(update, context):
   
    text = ('Olá, eu sou o assistente de operação da ALTAVE. Estou aqui para te'\
            ' ajudar com o seu chamado. Por favor, escolha sobre o que você deseja reportar.')
    buttons = [[
        InlineKeyboardButton(text='Operador', callback_data=str(ADD_OPERADOR)),
        InlineKeyboardButton(text='Software', callback_data=str(ADD_SOFTWARE))
    ], [
        InlineKeyboardButton(text='Equipamento', callback_data=str(ADD_EQUIPAMENTO)),
        InlineKeyboardButton(text='Fim', callback_data=str(END))
    ]]
    keyboard = InlineKeyboardMarkup(buttons)

    # If we're starting over we don't need do send a new message
    if context.user_data.get(START_OVER):
        update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        update.message.reply_text('Olá, eu sou o assistente de operação da ALTAVE. Estou aqui para te'\
                                  ' ajudar com o seu chamado. Por favor, escolha sobre o que você deseja reportar.')
        update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False
    return SELECIONANDO_AREA

# Definindo o primeiro nivel - segundo filtro

def seleciona_operador(update, context):
    
    text = 'Escolha entre um dos operadores'
    buttons = [[
        InlineKeyboardButton(text='Bruno', callback_data=str(BRUNO)),
        InlineKeyboardButton(text='Leando', callback_data=str(LEANDRO))
    ], [
        InlineKeyboardButton(text='Valdinir', callback_data=str(RAFAEL)),
        InlineKeyboardButton(text='Rafael', callback_data=str(VALDINIR))
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
                    
    return SELECIONA_OPERADOR

def seleciona_software(update, context):
    
    text = 'Selecione entre um dos softwares desenvolvidos pela ALTAVE'
    buttons = [[
        InlineKeyboardButton(text='Harpia (Visualizador)', callback_data=str(HARPIA)),
        InlineKeyboardButton(text='Tupan (Clima)', callback_data=str(TUPAN))
    ], [
        InlineKeyboardButton(text='Sauron (Reconhecimento)', callback_data=str(SAURON)),
        InlineKeyboardButton(text='Geocam (Controle do GPS)', callback_data=str(GEOCAM))
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
          
    
    return SELECIONA_SOFTWARE

def seleciona_equipamento(update, context):
    text = 'Selecione entre um dos softwares desenvolvidos pela ALTAVE'
    buttons = [[
        InlineKeyboardButton(text='Balao', callback_data=str(BALAO)),
        InlineKeyboardButton(text='Guincho', callback_data=str(GUINCHO))
    ], [
        InlineKeyboardButton(text='Gondola', callback_data=str(GONDOLA)),
        InlineKeyboardButton(text='Cabo de ancoragem', callback_data=str(CABO_EM))
    ], [
        InlineKeyboardButton(text='Caixa de dados', callback_data=str(CDG)),
        InlineKeyboardButton(text='Caixa do guincho', callback_data=str(CEG))
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
          
    
    return SELECIONA_EQUIPAMENTO

#Segundo nivel
    
def input_pn(update, context):
    context.user_data[CURRENT_FEATURE] = update.callback_query.data
    text = 'Informe o numero de serie do equipamento a ser reparado'
    update.callback_query.edit_message_text(text=text)
    
    return INPUT_PN

def salva_input(update, context):
    """Save input for feature and return to feature selection."""
    ud = context.user_data
    ud[FEATURES][ud[CURRENT_FEATURE]] = update.message.text

    ud[START_OVER] = True

    return SALVA_INPUT

def seleciona_saude(update, context):
    text = 'Selecione a situacao que deseja reportar.'
    buttons = [[
        InlineKeyboardButton(text='Mudar responsavel pela operacao', callback_data=str(RESPONSAVEL))
    ], [
        InlineKeyboardButton(text='Informar troca de operador', callback_data=str(OPERADOR))
    ], [
        InlineKeyboardButton(text='Acidente, emergencia ou mal estar', callback_data=str(SAUDE))
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
          
    
    return SELECIONA_SAUDE

def seleciona_bo_soft(update,context):
    text = 'Selecione a area relacionada ao seu problema'
    buttons = [[
        InlineKeyboardButton(text='Acesso', callback_data=str(ACESSO))
    ], [
        InlineKeyboardButton(text='Senha', callback_data=str(SENHA))
    ], [
        InlineKeyboardButton(text='Local', callback_data=str(LOCAL))
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return SELECIONA_BO_SOFT

def stop(update, context):
    """End Conversation by command."""
    update.message.reply_text('Okay, bye.')

    return END


def end(update, context):
    """End conversation from InlineKeyboardButton."""
    text = 'See you around!'
    update.callback_query.edit_message_text(text=text)

    return END


#def _name_switcher(level):
#    if level == PARENTS:
#        return ('Father', 'Mother')
#    elif level == CHILDREN:
#        return ('Brother', 'Sister')
#
#def select_gender(update, context):
#    """Choose to add mother or father."""
#    level = update.callback_query.data
#    context.user_data[CURRENT_LEVEL] = level
#
#    text = 'Please choose, whom to add.'
#
#    male, female = _name_switcher(level)
#
#    buttons = [[
#        InlineKeyboardButton(text='Add ' + male, callback_data=str(MALE)),
#        InlineKeyboardButton(text='Add ' + female, callback_data=str(FEMALE))
#    ], [
#        InlineKeyboardButton(text='Show data', callback_data=str(SHOWING)),
#        InlineKeyboardButton(text='Back', callback_data=str(END))
#    ]]
#
#    keyboard = InlineKeyboardMarkup(buttons)
#    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
#
#    return SELECTING_GENDER
#
#
#def end_second_level(update, context):
#    """Return to top level conversation."""
#    context.user_data[START_OVER] = True
#    start(update, context)
#
#    return END
    
# Error handler
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("863859400:AAHePje4fFREUqhThSd3xhOMqMSNtDkCroY", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

#    # Set up third level ConversationHandler (collecting features)
#    description_conv = ConversationHandler(
#        entry_points=[CallbackQueryHandler(select_feature,
#                                           pattern='^' + str(MALE) + '$|^' + str(FEMALE) + '$')],
#
#        states={
#            SELECTING_FEATURE: [CallbackQueryHandler(ask_for_input,
#                                                     pattern='^(?!' + str(END) + ').*$')],
#            TYPING: [MessageHandler(Filters.text, save_input)],
#        },
#
#        fallbacks=[
#            CallbackQueryHandler(end_describing, pattern='^' + str(END) + '$'),
#            CommandHandler('stop', stop_nested)
#        ],
#
#        map_to_parent={
#            # Return to second level menu
#            END: SELECTING_LEVEL,
#            # End conversation alltogether
#            STOPPING: STOPPING,
#        }
#    )
#
#    # Set up second level ConversationHandler (adding a person)
#    add_member_conv = ConversationHandler(
#        entry_points=[CallbackQueryHandler(select_level,
#                                           pattern='^' + str(ADDING_MEMBER) + '$')],
#
#        states={
#            SELECTING_LEVEL: [CallbackQueryHandler(select_gender,
#                                                   pattern='^{0}$|^{1}$'.format(str(PARENTS),
#                                                                                str(CHILDREN)))],
#            SELECTING_GENDER: [description_conv]
#        },
#
#        fallbacks=[
#            CallbackQueryHandler(show_data, pattern='^' + str(SHOWING) + '$'),
#            CallbackQueryHandler(end_second_level, pattern='^' + str(END) + '$'),
#            CommandHandler('stop', stop_nested)
#        ],
#
#        map_to_parent={
#            # After showing data return to top level menu
#            SHOWING: SHOWING,
#            # Return to top level menu
#            END: SELECTING_ACTION,
#            # End conversation alltogether
#            STOPPING: END,
#        }
#    )
    
    #Set segundo nivel
    conv_entrada = ConversationHandler(
            entry_points=[CallbackQueryHandler(seleciona_saude, pattern='^' + str(SELECIONA_OPERADOR) + '$'),
                          CallbackQueryHandler(seleciona_bo_soft, pattern='^' + str(SELECIONA_SOFTWARE) + '$'),
                          CallbackQueryHandler(input_pn, pattern='^' + str(SELECIONA_EQUIPAMENTO) + '$')
                          ],
            
            states = {
                    
            },
            fallbacks=[],
        )

    # Set up top level ConversationHandler (selecting action)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            SELECIONANDO_AREA: [
                CallbackQueryHandler(seleciona_operador, pattern='^' + str(ADD_OPERADOR) + '$'),
                CallbackQueryHandler(seleciona_equipamento, pattern='^' + str(ADD_EQUIPAMENTO) + '$'),
                CallbackQueryHandler(seleciona_software, pattern='^' + str(ADD_SOFTWARE) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(END) + '$')
            ],
        },

        fallbacks=[CommandHandler('stop', stop)],
    )
    # Because the states of the third level conversation map to the ones of the
    # second level conversation, we need to be a bit hacky about that:
#    conv_handler.states[SELECTING_LEVEL] = conv_handler.states[SELECTING_ACTION]
#    conv_handler.states[STOPPING] = conv_handler.entry_points

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