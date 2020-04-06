#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:21:46 2020
@author: beatrizsilva
"""


import logging
import telebot

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

#Estados do segundo nivel
INPUT_PN, SALVA_INPUT, SELECIONA_SAUDE, SELECIONA_BO_SOFT = map(chr, range(7,11))

#Estados do terceiro nivel
(BO_BALAO, BO_GUINCHO, BO_GONDOLA, BO_CABO_EM, BO_CDG, BO_CEG, BO_BERCO_SOLO,
 BO_BERCO_PIZZA, BO_SAURON, BO_HARPIA, BO_TUPAN, BO_GEOCAM, NYLON, PU, BALIZA, 
 DEFLACAO, SAIA, CORDAS) = map(chr, range(11,29))
#Constantes do terceiro nível
(TAMBOR, MOTOR, BOTOEIRA, PONTEIRA, PATAS, ANCORAS, SLIPRING, SPOT, PLC_GON, SWITCH_GON,
POWER_GON, DIAGRAMA_GON, CONECTOR_EM, PIGTAIL_FAB, PIGTAIL_REMEN, PLC_CDG, DISJUNTOR_CDG,
SWITCH_CDG, STECK, AGUA_CDG, ANCORAS, ENCAIXES, PARAFUSOS_BERCO, CINTAS, PIZZA, ENCAIXE_PIZZA,
ACESSO_SAURON, STREAMING_SAURON, TUTORIAL_SAURON, ACESSO_HARPIA, STREAMING_HARPIA, TUTORIAL_HARPIA,
CREDENCIAIS_HARPIA, LINK_HARPIA, ACESSO_TUPAN, LINK_TUPAN, ERRO_TUPAN, ERRO_1_GEOCAM,
ERRO_2_GEOCAM, TUTORIAL_GEOCAM) = map(chr, range(29,69))

# Constantes
(START_OVER, BRUNO, LEANDRO, VALDINIR, RAFAEL, BALAO, GUINCHO, GONDOLA, CDG, CEG,
 CABO_EM, BERCO_SOLO, BERCO_PIZZA, HARPIA, TUPAN, SAURON, GEOCAM, FEATURES, CURRENT_FEATURE, RESPONSAVEL,
 OPERADOR, SAUDE, ACESSO, SENHA, LOCAL) = map(chr, range(69, 94))

# Meta states
STOPPING, SHOWING = map(chr, range(94, 96))

# Shortcut for ConversationHandler.END
END = ConversationHandler.END



# Primeiro nível da conversa. Escolha entre área de ajuda
def start(update, context):
   
    text = ('Olá, eu sou o assistente de operação da ALTAVE. Estou aqui para te'\
            ' ajudar com o seu chamado.')
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
        update.message.reply_text('Por favor, escolha sobre o que você deseja reportar.')
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
    text = 'Selecione entre um dos hardware desenvolvidos pela ALTAVE'
    buttons = [[
        InlineKeyboardButton(text='Balao', callback_data=str(BALAO)),
        InlineKeyboardButton(text='Guincho', callback_data=str(GUINCHO))
    ], [
        InlineKeyboardButton(text='Gondola', callback_data=str(GONDOLA)),
        InlineKeyboardButton(text='Cabo de ancoragem', callback_data=str(CABO_EM))
    ], [
        InlineKeyboardButton(text='Caixa de dados', callback_data=str(CDG)),
        InlineKeyboardButton(text='Caixa do guincho', callback_data=str(CEG))
        ], [
        InlineKeyboardButton(text='Berço de solo', callback_data=str(BERCO_SOLO)),
        InlineKeyboardButton(text='BErço da pizza/picape', callback_data=str(BERCO_PIZZA))
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
          
    
    return SELECIONA_EQUIPAMENTO



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
#
#def seleciona_bo_soft(update,context):
#    text = 'Selecione a area relacionada ao seu problema'
#    buttons = [[
#        InlineKeyboardButton(text='Acesso', callback_data=str(ACESSO))
#    ], [
#        InlineKeyboardButton(text='Senha', callback_data=str(SENHA))
#    ], [
#        InlineKeyboardButton(text='Local', callback_data=str(LOCAL))
#    ]]
#    keyboard = InlineKeyboardMarkup(buttons)
#    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
#
#    return SELECIONA_BO_SOFT

# Terceiro nível - identificação dos problemas de hardware

    
def input_pn(update, context):
    context.user_data[CURRENT_FEATURE] = update.callback_query.data
    text = 'Vamos registrar o ocorrido? Informe o numero de serie do equipamento a ser reparado.'
    update.callback_query.edit_message_text(text=text)

    return INPUT_PN

def salva_input(update, context):
    """Save input for feature and return to feature selection."""
    ud = context.user_data
    ud[FEATURES][ud[CURRENT_FEATURE]] = update.message.text

    ud[START_OVER] = True
    
    return seleciona_equipamento(update, context)


def problemas_balao(update, context):
    text = 'Foi onde?'
    buttons = [[
        InlineKeyboardButton(text='Envelope externo', callback_data=str(NYLON), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
        InlineKeyboardButton(text='Envelope interno', callback_data=str(PU), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ], [
        InlineKeyboardButton(text='Balizas', callback_data=str(BALIZA), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
        InlineKeyboardButton(text='Deflação', callback_data=str(DEFLACAO), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ], [
        InlineKeyboardButton(text='Saia', callback_data=str(SAIA), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
        InlineKeyboardButton(text='Cordas', callback_data=str(CORDAS), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_BALAO


def tutorial_nylon(update, context):
    text = 'Foi onde?'
    InputFile(obj, filename=None, attach=None)
#    InputMediaVideo(media, caption=None, width=None, height=None, duration=None, supports_streaming=None, parse_mode=<telegram.utils.helpers.DefaultValue object>, thumb=None)
    buttons = [[
        InlineKeyboardButton(text='Envelope externo', callback_data=str(NYLON), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
        InlineKeyboardButton(text='Envelope interno', callback_data=str(PU), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ], [
        InlineKeyboardButton(text='Balizas', callback_data=str(BALIZA), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
        InlineKeyboardButton(text='Deflação', callback_data=str(DEFLACAO), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ], [
        InlineKeyboardButton(text='Saia', callback_data=str(SAIA), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
        InlineKeyboardButton(text='Cordas', callback_data=str(CORDAS), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_BALAO
    

def problemas_guincho(update,context):
    text = 'Qual parte?'
    buttons = [[
            InlineKeyboardButton(text='Tambor', callback_data=str(TAMBOR), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Motor', callback_data=str(MOTOR), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Botoeira', callback_data=str(BOTOEIRA), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Ponteira', callback_data=str(PONTEIRA), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Patas', callback_data=str(PATAS), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Ancoras', callback_data=str(ANCORAS), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Slipring', callback_data=str(SLIPRING), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    
    ]]
    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_GUINCHO


def problemas_gondola(update, context): #Incluir vanguarda e horizonte
    text = 'Onde está o problema? / O que deseja saber?'
    buttons = [[
            InlineKeyboardButton(text='Spot', callback_data=str(SPOT), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Pareamento do PLC', callback_data=str(PLC_GON), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Switch', callback_data=str(SWITCH_GON), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Energização', callback_data=str(POWER_GON), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Diagramas', callback_data=str(DIAGRAMA_GON), url='https://www.youtube.com/watch?v=7dKQWw96kcM')]]

    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_GONDOLA


def problemas_cabo(update, context):
    text = 'Onde está o problema? / O que deseja saber?'
    buttons = [[
            InlineKeyboardButton(text='Conserto de conector', callback_data=str(CONECTOR_EM), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Fabricação de pigtail', callback_data=str(PIGTAIL_FAB), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Remendo do pigtail', callback_data=str(PIGTAIL_REMEN), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ]]

    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_CABO_EM


def problemas_CDG(update, context):
    text = 'Qual componente?'
    buttons = [[
            InlineKeyboardButton(text='PLC', callback_data=str(PLC_CDG), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Disjuntor', callback_data=str(DISJUNTOR_CDG), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Switch', callback_data=str(SWITCH_CDG), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Conectores STECK', callback_data=str(STECK), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Água na caixa', callback_data=str(AGUA_CDG), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
#            InlineKeyboardButton(text='', callback_data=str())
#    ],  [
#            InlineKeyboardButton(text='', callback_data=str()),
#            InlineKeyboardButton(text='', callback_data=str())
    ]]

    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_CDG


#def problemas_CEG(update, context):
#    text = 'Qual componente?'
#    buttons = [[
#            InlineKeyboardButton(text='Disjuntor', callback_data=str()),
#            InlineKeyboardButton(text='Botoeira', callback_data=str())
#    ],  [
#            InlineKeyboardButton(text='', callback_data=str()),
#            InlineKeyboardButton(text='', callback_data=str())
#    ],  [
#            InlineKeyboardButton(text='', callback_data=str()),
#            InlineKeyboardButton(text='', callback_data=str())
#    ],  [
#            InlineKeyboardButton(text='', callback_data=str()),
#            InlineKeyboardButton(text='', callback_data=str())
#    ]]
#
#    keyboard = InlineKeyboardMarkup(buttons)
#    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
#
#    return BO_CEG


def problemas_berco_solo(update, context):
    text = 'Onde está o problema?'
    buttons = [[
            InlineKeyboardButton(text='Ancoras', callback_data=str(ANCORAS), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Encaixes', callback_data=str(ENCAIXES), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Parafusos', callback_data=str(PARAFUSOS_BERCO), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Cintas', callback_data=str(CINTAS), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ]]

    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_BERCO_SOLO


def problemas_berco_pizza(update, context):
    text = 'Qual componente?'
    buttons = [[
            InlineKeyboardButton(text='Ancoras', callback_data=str(ANCORAS), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Encaixes', callback_data=str(ENCAIXES), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Parafusos', callback_data=str(PARAFUSOS_BERCO), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Cintas', callback_data=str(CINTAS), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Prato da pizza', callback_data=str(PIZZA), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Encaixes da pizza', callback_data=str(ENCAIXE_PIZZA), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ]]

    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_BERCO_PIZZA

# Terceiro nível - identificação dos problemas de software
    
def bo_sauron(update, context):
    text = 'Qual componente?'
    buttons = [[
            InlineKeyboardButton(text='Acesso', callback_data=str(ACESSO_SAURON), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Streaming', callback_data=str(STREAMING_SAURON), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Tutorial completo', callback_data=str(TUTORIAL_SAURON), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ]]

    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_SAURON

def bo_harpia(update, context):
    text = 'Qual componente?'
    buttons = [[
            InlineKeyboardButton(text='Acesso', callback_data=str(ACESSO_HARPIA), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Streaming', callback_data=str(STREAMING_HARPIA), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Tutorial completo', callback_data=str(TUTORIAL_HARPIA), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Credenciais', callback_data=str(CREDENCIAIS_HARPIA), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Link', callback_data=str(LINK_HARPIA), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ]]

    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_HARPIA

def bo_tupan(update, context):
    text = 'Qual componente?'
    buttons = [[
            InlineKeyboardButton(text='Acesso', callback_data=str(ACESSO_TUPAN), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='Link', callback_data=str(LINK_TUPAN), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Erro no Tupan', callback_data=str(ERRO_TUPAN), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ]]

    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_TUPAN
    

def bo_geocam(update, context):
    text = 'Qual componente?'
    buttons = [[
            InlineKeyboardButton(text='ERRO 1', callback_data=str(ERRO_1_GEOCAM), url='https://www.youtube.com/watch?v=7dKQWw96kcM'),
            InlineKeyboardButton(text='ERRO 2', callback_data=str(ERRO_2_GEOCAM), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ],  [
            InlineKeyboardButton(text='Tutorial completo', callback_data=str(TUTORIAL_GEOCAM), url='https://www.youtube.com/watch?v=7dKQWw96kcM')
    ]]

    keyboard = InlineKeyboardMarkup(buttons)
    update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

    return BO_GEOCAM




#########################################################################################################

def stop(update, context):
    """End Conversation by command."""
    update.message.reply_text('Ta bom, tchau.')

    return END


def end(update, context):
    """End conversation from InlineKeyboardButton."""
    text = 'Te vejo por ai!'
    update.callback_query.edit_message_text(text=text)

    return END


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
#########################################################################################################

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    TOKEN = "863859400:AAHePje4fFREUqhThSd3xhOMqMSNtDkCroY"
    updater = Updater(TOKEN, use_context=True)
#    bot = TeleBot(TOKEN) 

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    

    entra_pn =  ConversationHandler(
        entry_points=[CallbackQueryHandler(input_pn,
                                           pattern='^' + str(END) + '$')],
            
        states={
            INPUT_PN: [MessageHandler(Filters.all, salva_input)],
        },

        fallbacks=[CommandHandler('stop', stop)],

#        map_to_parent={
#            # Return to second level menu
#            END: SELECTING_LEVEL,
#            # End conversation alltogether
#            STOPPING: STOPPING,
#        }
    )
            
            
########################################################################################################
            
    #Set terceiro nivel
    
    
########################################################################################################
            
    #Set segundo nivel

    add_software = ConversationHandler(
        entry_points=[CallbackQueryHandler(seleciona_software, pattern='^' + str(ADD_SOFTWARE) + '$')],

        states={
            SELECIONA_SOFTWARE: [CallbackQueryHandler(bo_sauron, pattern='^' + str(SAURON) + '$'),
                                CallbackQueryHandler(bo_harpia, pattern='^' + str(HARPIA) + '$'),
                                CallbackQueryHandler(bo_tupan, pattern='^' + str(TUPAN) + '$'),
                                CallbackQueryHandler(bo_geocam, pattern='^' + str(GEOCAM) + '$'),
                                 CallbackQueryHandler(end, pattern='^' + str(END) + '$')
           
            ]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )


    add_equipamento = ConversationHandler(
        entry_points=[CallbackQueryHandler(seleciona_equipamento, pattern='^' + str(ADD_EQUIPAMENTO) + '$')],

        states={
            SELECIONA_EQUIPAMENTO: [entra_pn,
                CallbackQueryHandler(problemas_balao, pattern='^' + str(BALAO) + '$'),
                CallbackQueryHandler(problemas_guincho, pattern='^' + str(GUINCHO) + '$'),
                CallbackQueryHandler(problemas_gondola, pattern='^' + str(GONDOLA) + '$'),
                CallbackQueryHandler(problemas_cabo, pattern='^' + str(CABO_EM) + '$'),
                CallbackQueryHandler(problemas_CDG, pattern='^' + str(CDG) + '$'),
                CallbackQueryHandler(problemas_berco_solo, pattern='^' + str(BERCO_SOLO) + '$'),
                CallbackQueryHandler(problemas_berco_pizza, pattern='^' + str(BERCO_PIZZA) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(END) + '$')]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )


    add_operador = ConversationHandler(
        entry_points=[CallbackQueryHandler(seleciona_operador, pattern='^' + str(ADD_OPERADOR) + '$')],

        states={
            SELECIONA_OPERADOR: [CallbackQueryHandler(seleciona_saude,
                                                   pattern='^{0}$|^{1}$'.format(str(BRUNO),
                                                                                str(LEANDRO),
                                                                                str(RAFAEL),
                                                                                str(VALDINIR))),
                                 CallbackQueryHandler(end, pattern='^' + str(END) + '$')
            ]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )
#########################################################################################################

    # Set up top level ConversationHandler (selecting action)

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            SELECIONANDO_AREA: [add_operador, add_equipamento, add_software,
                CallbackQueryHandler(end, pattern='^' + str(END) + '$')
            ]
        },

        fallbacks=[CommandHandler('stop', stop)]
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