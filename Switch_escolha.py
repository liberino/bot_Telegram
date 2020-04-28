import logging

from telegram import (InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup,
                      ReplyKeyboardRemove, MessageEntity)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)
# send_document está sendo utilizaod para enviar os arquivos em pdf. O tamanho máximo dos arquivos deve
# ser 50 MB
# The document argument can be either a file_id, an URL or a file from disk 
#Procedimento_de_Purge = open(Procedimento_de_Purge.pdf, 'r')
def acesso(software):
    user = update.message.from_user
    chat_id = update.message.chat_id
    document = open('Procedimento_de_Purge.pdf', 'rb')
    funil = {
        "Sauron": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Harpia": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Tupan": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Geocam": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs)
    }
    return ACESSO

def streaming(software):
    user = update.message.from_user
    chat_id = update.message.chat_id
    document = open('Procedimento_de_Purge.pdf', 'rb')
    funil = {
        "Sauron": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Harpia": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Tupan": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Geocam": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs)
    }
    return STREAMING

def tutorial_completo(software):
    user = update.message.from_user
    chat_id = update.message.chat_id
    document = open('Procedimento_de_Purge.pdf', 'rb')
    funil = {
        "Sauron": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Harpia": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Tupan": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Geocam": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs)
    }
    return TUTORIAL_COMPLETO

def reporta_erro(software):
    user = update.message.from_user
    chat_id = update.message.chat_id
    document = open('Procedimento_de_Purge.pdf', 'rb')
    funil = {
        "Sauron": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Harpia": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Tupan": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Geocam": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs)
    }
    return REPORTA_ERRO

def dicionario_tutoriais(software):
    user = update.message.from_user
    chat_id = update.message.chat_id
    document = open('Procedimento_de_Purge.pdf', 'rb')
    funil = {
        "Sauron": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Harpia": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Tupan": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Geocam": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs)
    }
    return DICIONARIO_TUTORIAIS

def credenciais(software):
    user = update.message.from_user
    chat_id = update.message.chat_id
    document = open('Procedimento_de_Purge.pdf', 'rb')
    funil = {
        "Sauron": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Harpia": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Tupan": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Geocam": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs)
    }
    return CREDENCIAIS

def link(software):
    user = update.message.from_user
    chat_id = update.message.chat_id
    document = open('Procedimento_de_Purge.pdf', 'rb')
    funil = {
        "Sauron": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Harpia": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Tupan": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Geocam": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs)
    }
    return LINK

def debug(software):
    user = update.message.from_user
    chat_id = update.message.chat_id
    document = open('Procedimento_de_Purge.pdf', 'rb')
    funil = {
        "Sauron": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Harpia": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Tupan": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Geocam": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs)
    }
    return DEBUG

def add_tutorial(software):
    user = update.message.from_user
    chat_id = update.message.chat_id
    document = open('Procedimento_de_Purge.pdf', 'rb')
    funil = {
        "Sauron": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Harpia": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Tupan": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs),
        "Geocam": context.bot.send_document(chat_id, document=document, filename='Procedimento de Purge', caption='Também disponível em vídeo',
                                        disable_notification=False, reply_to_message_id=None,
                                        reply_markup=None, timeout=None, parse_mode=None, thumb=None, **kwargs)
    }
    return ADD_TUTORIAL
    

def switch_escolha(escolha):
    user = update.message.from_user
    chat_id = update.message.chat_id
    switcher = {
        "Acesso": acesso,
        "Streaming": streaming,
        "Tutorial Completo": tutorial_completo,
        "Acusar Erro": acusa_erro,
        "Outros tutoriais": dicionario_tutoriais,
        "Credenciais": credenciais,
        "Link de acesso": link,
        "Debug": debug,
        "Adicionar_tutorial": add_tutorial
    }
    return ESCOLHE_SUBAREA