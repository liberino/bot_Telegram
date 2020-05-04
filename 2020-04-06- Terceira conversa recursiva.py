#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:23:01 2020

@author: beatrizsilva
"""

import logging

from PyPDF2 import PdfFileWriter, PdfFileReader

from telegram import (InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup,
                      ReplyKeyboardRemove, MessageEntity)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)

from Banco_tutoriais_fixos_softwares import switcher, url

from Opcoes_equipamentos import Tutoriais, url_tutoriais

from checklists_altave import checklists_manutencao

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

#Estados de redirecionamento de equipamentos
(REDIRECIONA_EQUIPAMENTO, N_SERIE_ANTIGO, N_SERIE_NOVO,
TUTORIAL_BALAO, TUTORIAL_GUINCHO, TUTORIAL_GONDOLA, TUTORIAL_CABO, TUTORIAL_CDG,
TUTORIAL_CEG, TUTORIAL_BERCO, TUTORIAL_PIZZA, TUTORIAIS, N_SERIE_DEFEITO, ID_MANUTENCAO,
CHECK_LISTS, ESCOLHE_SUBAREA_EQ) = map(chr, range(29,45))

#Estados de redirecionamento da operação
ATUALIZA_RESPONSAVEL, ATUALIZA_OPERADOR = map(chr, range(45,47))

# Meta states
STOPPING, SHOWING = map(chr, range(47, 49))

# Shortcut for ConversationHandler.END
END = ConversationHandler.END

def start(update, context):
    user = update.message.from_user
    mensagem = update.message.text
    
    
    if mensagem == '/voltar':
        reply_keyboard = [['Operação', 'Software', 'Equipamento', 'Encaminhar registro']]
    
        update.message.reply_text(
            'Por favor, escolha sobre o que você deseja reportar. Você pode cancelar o chamado'\
            ' a qualquer momento com /termina',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        logger.info("%s %s abriu chamado", user.first_name, user.last_name)
        
        
    else: 
        
        reply_keyboard = [['Operação', 'Software', 'Equipamento', 'Encaminhar registro']]
        
        update.message.reply_text(
            'Olá, eu sou o assistente de operação da ALTAVE. Estou aqui para te'\
            ' ajudar com o seu chamado. '\
            'Por favor, escolha sobre o que você deseja reportar.',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        logger.info("%s %s abriu chamado", user.first_name, user.last_name)
        
        w = open("Registro_assistencia.txt", 'a')
        
        
    return SELECIONANDO_AREA

def selecionando_area(update, context):
    user = update.message.from_user
    area = update.message.text
     
    if area == 'Operação':
         
        user = update.message.from_user
        reply_keyboard = [['Mudar responsável pela operação'],
        ['Informar troca de operador']]
        
        update.message.reply_text(
                'Selecione uma das ações',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

        logger.info("%s reporta sobre %s", user.first_name, update.message.text)

        return SELECIONA_OPERADOR
    
    elif area == 'Software':

        user = update.message.from_user
        reply_keyboard = [['Harpia', 'Tupan'],
                ['Sauron', 'Geocam']]
    
        update.message.reply_text(
                'Selecione entre um dos softwares desenvolvidos pela ALTAVE',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

        logger.info("%s reporta sobre %s", user.first_name, update.message.text)
        user = update.message.from_user
    
        return SELECIONA_SOFTWARE
    
    elif area == 'Equipamento':
        
        user = update.message.from_user
        reply_keyboard = [['Balão', 'Guincho', 'Gondola'],
                ['Cabo de ancoragem', 'Caixa de dados'],
                ['Caixa do guincho', 'Berço de solo', 'Berço da pizza/picape']]
        
        update.message.reply_text(
                'Selecione entre um dos hardware desenvolvidos pela ALTAVE',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        
        
        logger.info("%s reporta sobre %s", user.first_name, update.message.text)
        user = update.message.from_user
    
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
            
        return start
 
def encaminha_ajuda(update, context):

    user = update.message.from_user
    chat_id = update.message.chat_id
    logger.info("%s %s está pedindo ajuda para o Inaldo: %s", user.first_name, user.last_name, update.message.text)
    
    # Trocar por contato de emergência da operação
    context.bot.sendMessage('582892178', 'Olá Inaldo, sua equipe precisa falar com você!',
                        parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                        reply_to_message_id=None, reply_markup=None, timeout=None)
    
    context.bot.forwardMessage(chat_id='582892178', from_chat_id=update.message.chat_id,
                                message_id=update.message.message_id)
    
    context.bot.sendMessage(chat_id, 'Beleza! Enviei sua mensagem para ele. Espera um pouco que ele já entra em contato com você.',
                    parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                    reply_to_message_id=None, reply_markup=None, timeout=None)
    
    logger.info("%s %s terminou seu pedido", user.first_name, user.last_name)
    
    return AJUDA_OPERACOES

################################
# Encaminha problemas de software, supõe que os problemas são todos da mesma grande natureza e salva as entradas anteriores
# Chamar o estado SELECIONA_SOFTWARE para esse estado

def seleciona_software(update,context):
    software = update.message.text
    user = update.message.from_user
    
    reply_keyboard = [['Acesso '+ software, 'Streaming '+ software, 'Credenciais '+ software],
            ['Link de acesso '+ software, 'Debug '+ software,'Outros tutoriais '+ software],
            ['Acusar Erro_'+ software, 'Tutorial Completo '+ software, 'Adicionar tutorial '+ software]]

    logger.info("%s reporta sobre %s", user.first_name, software)
    update.message.reply_text(
            'Então, vamos lá! Como posso te ajudar? Escolha uma das opções para obter um guia, vá em Debug para '\
            'obter resolução para os problemas mais frequentes, Acusar erro para enviar uma mensagem pelo responsável '\
            'Tutorial completo para obter um guia básico para usar o sistema. A função de adicionar tutorial só está disponível '\
            'para desenvolvedores, beleza?!',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
                
    return REDIRECIONA_SOFTWARE

def redireciona_software(update,context):
    user = update.message.from_user
    escolha = update.message.text
    escolha_erro = escolha.split("_")[0]
    chat_id = update.message.chat_id
    
    if escolha_erro == 'Acusar Erro':
    
        # Trocar por id da vitória
        context.bot.sendMessage('582892178', 'Olá Vitória, estão acusando erro de Software!',
                            parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                            reply_to_message_id=None, reply_markup=None, timeout=None)
        
        #Trocar por id do guilherme
        context.bot.sendMessage('582892178', 'Olá Guilherme, estão acusando erro de Software!',
                            parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                            reply_to_message_id=None, reply_markup=None, timeout=None)
        
        #Trocar por id do leozinho
        context.bot.sendMessage('582892178', 'Olá Leonardo, estão acusando erro de Software!',
                            parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                            reply_to_message_id=None, reply_markup=None, timeout=None)
        
        context.bot.sendMessage(chat_id, 'Beleza! Sua mensagem foi encaminhada. Espera um pouco que alguém já entra em contato com você.',
                        parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                        reply_to_message_id=None, reply_markup=None, timeout=None)
    
    else:
        chat_id = update.message.chat_id
        context.bot.sendMessage(chat_id, 'Tá, vou te mandar um guia. Caso não te ajude, procure outro tutorial digitando /tutorial '\
                        'ou se quiser voltar ao início, digite /voltar',
                        parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                        reply_to_message_id=None, reply_markup=None, timeout=None)
        
        #for escolha in switcher:
        context.bot.send_document(chat_id, document=switcher[escolha], filename=escolha, caption='Também disponível em vídeo\n'+url[escolha],
                                    disable_notification=False, reply_to_message_id=None,
                                    reply_markup=None, timeout=None, parse_mode=None, thumb=None)
        
    return ESCOLHE_SUBAREA 

def volta_tutorial_software(update, context):
    user = update.message.from_user
    reply_keyboard = [['Harpia', 'Tupan'],
            ['Sauron', 'Geocam']]

    update.message.reply_text(
            'Selecione entre um dos softwares desenvolvidos pela ALTAVE',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    logger.info("Chamado não resolvido. %s reporta sobre %s", user.first_name, update.message.text)
    user = update.message.from_user

    return SELECIONA_SOFTWARE
################################

def seleciona_equipamento(update, context):
    
    user = update.message.from_user
    equipamento = update.message.text
    
    reply_keyboard = [['Troca do equipamento_'+ equipamento, 'Troca de componente_'+ equipamento],
         ['Tutoriais_'+ equipamento, 'Defeito_'+ equipamento],
         ['Manutenção_'+ equipamento]]
    
    update.message.reply_text(
        'Selecione uma opção ou aperte /voltar para retornar ao início. \n'
        'Troca do equipamento é para quando se troca todo o sistema ex: troca do guincho inteiro. \n'
        'Troca do componente é quando troca-se alguma coisa desse sistema ex: troca da pata \n'
        'Tutoriais você recebe uma lista de tutoriais disponíveis. Defeito é para registrar quando algo '
        'está estragado. \n Manutenção é o registro das manutenções dadas ao sistema.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
    logger.info("%s reporta sobre %s", user.first_name, equipamento)

    return REDIRECIONA_EQUIPAMENTO

def redireciona_equipamento(update, context):
    user  = update.message.from_user
    escolha_equipamento = update.message.text
    escolha = escolha_equipamento.split("_")[0]
    equipamento = escolha_equipamento.split("_")[1]
    
    if escolha == 'Troca do equipamento':
        
        logger.info("%s está reportando %s de %s", user.first_name, escolha, equipamento)
        
        update.message.reply_text('Entendi. Me fale agora o número de série do equipamento antigo.')
        
        return N_SERIE_ANTIGO
        
    elif escolha == 'Troca de componente':
        
        logger.info("%s está reportando %s de %s", user.first_name, escolha, equipamento)
        
        update.message.reply_text('Entendi. Me fale agora o número de série do equipamento antigo.')
        
        return N_SERIE_ANTIGO
    
    elif escolha == 'Tutoriais':
        
        if equipamento == 'Balão':
            
            user = update.message.from_user
            reply_keyboard = [['Abastecimento', 'Transfusão', 'Teste da Baliza'],
                    ['Reparo no PU', 'Reparo no Nylon'],
                    ['Troca do cartucho da deflação', 'Outros_'+equipamento]]
        
            logger.info("%s procura tutorial sobre %s", user.first_name, update.message.text)
            update.message.reply_text(
                    'Selecione entre um dos tutoriais ou veja a lista completa em Outros',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
            return TUTORIAL_BALAO
            
        elif equipamento == 'Guincho':
            
            user = update.message.from_user
            reply_keyboard = [['Manual de montagem_'+equipamento, 'Teste elétrico_'+equipamento],
                    ['Manual de manutenção mensal_'+equipamento, 'Manual de manutenção semestral_'+equipamento],
                    ['Outros_'+equipamento]]
        
            logger.info("%s procura tutorial sobre %s", user.first_name, update.message.text)
            update.message.reply_text(
                    'Selecione entre um dos tutoriais ou veja a lista completa em Outros',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
            return TUTORIAL_GUINCHO
            
        elif equipamento == 'Gondola':
            
            user = update.message.from_user
            reply_keyboard = [['Teste da deflação', 'Pareamento do PLC', 'Teste do SPOT'],
                    ['Verificação da conexão (PING)', 'Diagrama elétrico_'+equipamento],
                    ['Manual de montagem_'+equipamento,'Outros_'+equipamento]]
        
            logger.info("%s procura tutorial sobre %s", user.first_name, update.message.text)
            update.message.reply_text(
                    'Selecione entre um dos tutoriais ou veja a lista completa em Outros',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
            return TUTORIAL_GONDOLA
            
        elif equipamento == 'Cabo de ancoragem':
            
            user = update.message.from_user
            reply_keyboard = [['Reparo do conector_'+equipamento],
                    ['Reparo do stopper'],
                    ['Outros_'+equipamento]]
        
            logger.info("%s procura tutorial sobre %s", user.first_name, update.message.text)
            update.message.reply_text(
                    'Selecione entre um dos tutoriais ou veja a lista completa em Outros',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
            return TUTORIAL_CABO
            
        elif equipamento == 'Caixa de dados':
            
            user = update.message.from_user
            reply_keyboard = [['Pareamento do PLC', 'Manual de montagem_'+equipamento],
                    ['Diagrama elétrico_'+equipamento],
                    ['Outros_'+equipamento]]
        
            logger.info("%s procura tutorial sobre %s", user.first_name, update.message.text)
            update.message.reply_text(
                    'Selecione entre um dos tutoriais ou veja a lista completa em Outros',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
            return TUTORIAL_CDG
            
        elif equipamento == 'Caixa do guincho':
            
            user = update.message.from_user
            reply_keyboard = [['Manual de montagem_'+equipamento, 'Diagrama elétrico_'+equipamento],
                    ['Outros_'+equipamento]]
        
            logger.info("%s procura tutorial sobre %s", user.first_name, update.message.text)
            update.message.reply_text(
                    'Selecione entre um dos tutoriais ou veja a lista completa em Outros',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
            return TUTORIAL_CEG
            
        elif equipamento == 'Berço de solo':
            
            user = update.message.from_user
            reply_keyboard = [['Instalação de ancoras', 'Manual de montagem_'+equipamento],
                    ['Outros_'+equipamento]]
        
            logger.info("%s procura tutorial sobre %s", user.first_name, update.message.text)
            update.message.reply_text(
                    'Selecione entre um dos tutoriais ou veja a lista completa em Outros',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
            return TUTORIAL_BERCO
            
        else:
            
            user = update.message.from_user
            reply_keyboard = [['Manual de montagem_'+equipamento, 'Picapes compatíveis'],
                    ['Outros_'+equipamento]]
        
            logger.info("%s procura tutorial sobre %s", user.first_name, update.message.text)
            update.message.reply_text(
                    'Selecione entre um dos tutoriais ou veja a lista completa em Outros',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
            return TUTORIAL_PIZZA
            
        return TUTORIAIS
        
    elif escolha == 'Defeito': 
        
        logger.info("%s está reportando %s de %s", user.first_name, escolha, equipamento)
        
        update.message.reply_text('Entendi. Me fale agora o número de série do equipamento defeituoso.')
        
        return N_SERIE_DEFEITO
    
    elif escolha == 'Manutenção':
        
        logger.info("%s está reportando %s de %s", user.first_name, escolha, equipamento)
        
        reply_keyboard = [['Todo o '+equipamento, 'Item do '+equipamento]]

        update.message.reply_text('Você fez a escolha certa! Manutenções garantem bom funcionamento e longevidade ao sistema. Me fale, você vai fazer manutenção em um item ou em todo '+ equipamento,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        
        return ID_MANUTENCAO
        
    else: 
        update.message.reply_text('Escolha uma opção da lista.')
        
        reply_keyboard = [['Troca do equipamento_'+ equipamento, 'Troca de componente_'+ equipamento],
         ['Tutoriais_'+ equipamento, 'Defeito_'+ equipamento],
         ['Manutenção_'+ equipamento]]
    
        update.message.reply_text(
            'Selecione uma opção ou aperte /voltar para retornar ao início. \n'
            'Troca do equipamento é para quando se troca todo o sistema ex: troca do guincho inteiro. \n'
            'Troca do componente é quando troca-se alguma coisa desse sistema ex: troca da pata\n'
            'Tutoriais você recebe uma lista de tutoriais disponíveis. Defeito é para registrar quando algo'
            'está estragado. \n Manutenção é o registro das manutenções dadas ao sistema.',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        
        logger.info("%s escreveu %s, o que não está na lista", user.first_name, escolha_equipamento)
                    
        return REDIRECIONA_EQUIPAMENTO
        
def n_serie_antigo(update, context):
    
    user = update.message.from_user
    n_serie_equipamento_antigo = update.message.text
    
    logger.info("O número de série do equipamento que %s vai trocar é %s", user.first_name, n_serie_equipamento_antigo)
        
    update.message.reply_text('Ótimo, muito obrigada. Me fale agora o número de série do equipamento novo.')
    
    return N_SERIE_NOVO
    
def n_serie_novo(update, context):
    
    user = update.message.from_user
    n_serie_equipamento_antigo = update.message.text
    
    logger.info("O número de série do equipamento que %s vai entrar é %s", user.first_name, n_serie_equipamento_antigo)
        
    update.message.reply_text('Você fez a escolha certa em ter me contado. Empresas que registram vão longe! \n Mais alguma coisa? Se sim, digite /voltar. Se não precisar então digite /terminei.')
    
    return ESCOLHE_SUBAREA 
    
def n_serie_defeito(update, context):
    
    user = update.message.from_user
    n_serie_equipamento_defeituoso = update.message.text
    
    logger.info("O número de série do equipamento defeituoso é %s",  n_serie_equipamento_defeituoso)
        
    update.message.reply_text('Você fez a escolha certa em ter me contado. Empresas que registram vão longe! \n Mais alguma coisa? Se sim, digite /voltar. Se não precisar então digite /terminei.')
    
    return ESCOLHE_SUBAREA 
        
def id_manutencao(update, context):
    
    user = update.message.from_user
    parte_manutencao = update.message.text
    
    reply_keyboard = [['Checklist de_'+parte_manutencao, 'Não precisa']]

    update.message.reply_text('Entendi. Obrigada pelo registro. Deseja um checklist?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        
    logger.info(" %s Informa manutenção em %s", user.first_name, parte_manutencao)
    
    return CHECK_LISTS

def check_lists(update, context):
    
    user  = update.message.from_user
    escolha_equipamento = update.message.text
    escolha = escolha_equipamento.split("_")[0]
    equipamento = escolha_equipamento.split("_")[1]
    
    if escolha == 'Checklist de':
        
        chat_id = update.message.chat_id
        
        context.bot.send_document(chat_id, document=checklists_manutencao[equipamento], filename=escolha_equipamento, caption='Aqui está! Termine seu chamado com /terminei',
                                disable_notification=False, reply_to_message_id=None,
                                reply_markup=None, timeout=None, parse_mode=None, thumb=None)
        
    else:
    
        return end
    
    return end

def tutoriais(update, context):
    
    user = update.message.from_user
    escolha = update.message.text
    # print(software)
    
    chat_id = update.message.chat_id
    context.bot.sendMessage(chat_id, 'Tá, vou te mandar um guia. Caso não te ajude, procure outro tutorial digitando /tutorial '\
                    'ou se quiser voltar ao início, digite /voltar',
                    parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                    reply_to_message_id=None, reply_markup=None, timeout=None)
    
    #for escolha in switcher:
    context.bot.send_document(chat_id, document=Tutoriais[escolha], filename=escolha, caption='Também disponível em vídeo\n'+url_tutoriais[escolha],
                                disable_notification=False, reply_to_message_id=None,
                                reply_markup=None, timeout=None, parse_mode=None, thumb=None)
        
    return ESCOLHE_SUBAREA_EQ

def volta_tutorial_equipamentos(update, context):
    user = update.message.from_user
    reply_keyboard = [['Balão', 'Guincho', 'Gondola'],
            ['Cabo de ancoragem', 'Caixa de dados'],
            ['Caixa do guincho', 'Berço de solo', 'Berço da pizza/picape']]
    
    update.message.reply_text(
            'Selecione entre um dos hardware desenvolvidos pela ALTAVE',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    
    logger.info("Chamado não resolvido. %s reporta sobre %s", user.first_name, update.message.text)
    user = update.message.from_user

    return SELECIONA_EQUIPAMENTO
################################

def seleciona_operador(update, context):
    
    user = update.message.from_user
    escolha = update.message.text
    if escolha == 'Mudar responsável pela operação':
    
        logger.info("%s %s está informando troca de responsável", user.first_name, user.last_name)
        update.message.reply_text('Entendi. Quem será o novo responsável?')
    
        return ATUALIZA_RESPONSAVEL
    
    elif escolha == 'Informar troca de operador':
        
        logger.info("%s %s está informando troca de operador", user.first_name, user.last_name)
        update.message.reply_text('Entendi. Me fale qual foi a troca em uma mesma mensagem. \n Ex: Bruno saiu e Leandro entrou.')
        
        return ATUALIZA_OPERADOR
    
    else:
        
        update.message.reply_text('Opção inválida, volte para o começo com \cancela')
        
        return start

def atualiza_responsavel(update, context):
    
    user = update.message.from_user
    chat_id = update.message.chat_id
    mensagem = update.message.text
    logger.info("%s %s está trocando o responsável pela operação para: %s", user.first_name, user.last_name, update.message.text)
    
    # Trocar por grupo de responsáveis pela operação
    context.bot.sendMessage('582892178', 'Olá, o responsável pela operação foi alterado.',
                        parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                        reply_to_message_id=None, reply_markup=None, timeout=None)
    
    context.bot.forwardMessage(chat_id='582892178', from_chat_id=update.message.chat_id,
                                message_id=update.message.message_id)
    
    context.bot.sendMessage(chat_id, 'Anotado! Obrigada por manter o registro atualizado.',
                    parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                    reply_to_message_id=None, reply_markup=None, timeout=None)
    
    logger.info("%s %s informou troca de responsável: %s", user.first_name, user.last_name, mensagem)

def atualiza_operador(update, context):
    
    user = update.message.from_user
    chat_id = update.message.chat_id
    mensagem = update.message.text
    logger.info("%s %s está trocando o responsável pela operação para: %s", user.first_name, user.last_name, update.message.text)
    
    # Trocar por grupo de responsáveis pela operação
    context.bot.sendMessage('582892178', 'Olá, houve troca de operador.',
                        parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                        reply_to_message_id=None, reply_markup=None, timeout=None)
    
    context.bot.forwardMessage(chat_id='582892178', from_chat_id=update.message.chat_id,
                                message_id=update.message.message_id)
    
    context.bot.sendMessage(chat_id, 'Anotado! Obrigada por manter o registro atualizado.',
                    parse_mode=None, disable_web_page_preview=None, disable_notification=False,
                    reply_to_message_id=None, reply_markup=None, timeout=None)
    
    logger.info("%s %s informou troca de operador: %s", user.first_name, user.last_name, mensagem)

#################################
def stop(update, context):
    """End Conversation by command."""
    user = update.message.from_user
    update.message.reply_text('Que pena! Espero ajudar da próxima vez. Tchau.')
    logger.info("Chamado não resolvido. %s cancelou seu chamado sobre %s", user.first_name, update.message.text)

    return END


def end(update, context):
    """End conversation from InlineKeyboardButton."""
    user = update.message.from_user
    text = 'Então tá bom. Te vejo por ai!'
    logger.info("%s teve seu chamado resolvido.", user.first_name)
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
            SELECIONANDO_AREA: [MessageHandler(Filters.regex('^(Operação|Software|Equipamento|Encaminhar registro)$'), selecionando_area),
                                CommandHandler('start', start),
                                CommandHandler('voltar', start),
                                CommandHandler('terminei', end),
                                CommandHandler('cancel', stop),
                                CommandHandler('end', end),
                                CommandHandler('finish', end)],
            AJUDA: [MessageHandler(Filters.regex('^Tenho certeza, chama o Inaldo.|Voltar$'), digita_ajuda),
                    CommandHandler('voltar', start),
                    CommandHandler('cancela', end,),
                    CommandHandler('recomeca', start),
                    CommandHandler('cancel', stop),
                    CommandHandler('end', end),
                    CommandHandler('finish', end)],
            ENCAMINHA_AJUDA: [MessageHandler(Filters.text, encaminha_ajuda)],
            SELECIONA_SOFTWARE: [MessageHandler(Filters.regex('^Harpia|Tupan|Sauron|Geocam$'), seleciona_software),
                                 CommandHandler('voltar', start),
                                 CommandHandler('cancel', stop),
                                 CommandHandler('end', end),
                                 CommandHandler('finish', end)],
            REDIRECIONA_SOFTWARE: [MessageHandler(Filters.regex('^Acesso|Streaming|Credenciais|Link de acesso|Debug|Outros tutoriais|Acusar Erro_|Tutorial Completo|Adicionar_tutorial$'), redireciona_software),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            ESCOLHE_SUBAREA: [CommandHandler('voltar', start),
                              CommandHandler('tutorial', volta_tutorial_software),
                              CommandHandler('cancel', stop),
                              CommandHandler('end', end),
                              CommandHandler('finish', end)],
            SELECIONA_EQUIPAMENTO: [MessageHandler(Filters.regex('^Balão|Guincho|Gondola|Cabo de ancoragem|Caixa de dados|Caixa do guincho|Berço de solo|Berço da pizza/picape$'), seleciona_equipamento),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            REDIRECIONA_EQUIPAMENTO: [MessageHandler(Filters.regex('^Troca do equipamento|Troca de componente|Tutoriais|Defeito|Manutenção$'), redireciona_equipamento),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            N_SERIE_ANTIGO: [MessageHandler(Filters.text, n_serie_antigo),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            N_SERIE_NOVO: [MessageHandler(Filters.text, n_serie_novo),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            N_SERIE_DEFEITO: [MessageHandler(Filters.text, n_serie_defeito),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            ID_MANUTENCAO: [MessageHandler(Filters.regex('^Todo o |Item do $'), id_manutencao),
                            CommandHandler('voltar', start),
                            CommandHandler('cancel', stop),
                            CommandHandler('end', end),
                            CommandHandler('finish', end)],
            CHECK_LISTS: [MessageHandler(Filters.regex('^Checklist de_|Não precisa$'), check_lists),
                          CommandHandler('voltar', start),
                          CommandHandler('cancel', stop),
                          CommandHandler('end', end),
                          CommandHandler('finish', end)],
            TUTORIAL_BALAO: [MessageHandler(Filters.regex('^Abastecimento|Transfusão|Teste da Baliza|Reparo no PU|Reparo no Nylon|Troca do cartucho da deflação|Outros_$'), tutoriais),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            TUTORIAL_BERCO: [MessageHandler(Filters.regex('^Instalação de ancoras|Manual de montagem_|Outros_$'), tutoriais),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            TUTORIAL_CABO: [MessageHandler(Filters.regex('^Reparo do conector_|Reparo do stopper|Outros_$'), tutoriais),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            TUTORIAL_CDG: [MessageHandler(Filters.regex('^Pareamento do PLC|Manual de montagem_|Diagrama elétrico_|Outros_$'), tutoriais),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            TUTORIAL_CEG: [MessageHandler(Filters.regex('^Manual de montagem_|Diagrama elétrico_|Outros_$'), tutoriais),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            TUTORIAL_GONDOLA: [MessageHandler(Filters.regex('^Teste da deflação|Pareamento do PLC|Teste do SPOT|Verificação da conexão (PING)|Diagrama elétrico_|Manual de montagem_|Outros_$'), tutoriais),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            TUTORIAL_GUINCHO: [MessageHandler(Filters.regex('^Manual de montagem_|Teste elétrico_|Manual de manutenção mensal_|Manual de manutenção semestral_|Outros_$'), tutoriais),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            TUTORIAL_PIZZA: [MessageHandler(Filters.regex('^Manual de montagem_|Picapes compatíveis|Outros_$'), tutoriais),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            ESCOLHE_SUBAREA_EQ: [CommandHandler('voltar', start),
                              CommandHandler('tutorial', volta_tutorial_equipamentos),
                              CommandHandler('cancel', stop),
                              CommandHandler('end', end),
                              CommandHandler('finish', end)],
            SELECIONA_OPERADOR: [MessageHandler(Filters.regex('^Mudar responsável pela operação|Informar troca de operador$'), seleciona_operador),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
           ATUALIZA_RESPONSAVEL: [MessageHandler(Filters.text, atualiza_responsavel),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
            ATUALIZA_OPERADOR: [MessageHandler(Filters.text, atualiza_operador),
                                    CommandHandler('voltar', start),
                                    CommandHandler('cancel', stop),
                                    CommandHandler('end', end),
                                    CommandHandler('finish', end)],
        },
 
        fallbacks=[CommandHandler('cancela', stop),
                   CommandHandler('terminei', end),
                   CommandHandler('cancel', stop),
                   CommandHandler('end', end),
                   CommandHandler('finish', end)]
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