user = update.message.from_user
        reply_keyboard = [['Bruno', 'Leando', 'Valdinir', 'Rafael']]
        
        update.message.reply_text(
                'Escolha entre um dos operadores',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

        logger.info("%s reporta sobre %s", user.first_name, update.message.text)

        return SELECIONA_OPERADOR

def responsavel(update, context):
    user = update.message.from_user
    logger.info("%s, você: escolheu mudar o responsável pela operação.", user.first_name, update.message.text)
    update.message.reply_text('Então, me mande o nome de quem será o novo responsável pela operação',
                              reply_markup=ReplyKeyboardRemove())
 
    return NOME_RESPONSAVEL

def nome_responsavel(update, context):
    user = update.message.from_user
    logger.info("Então %s, o nome do responsável é %s", user.first_name, update.message.text)
    update.message.reply_text('Entedi. Obrigada!')
 
    return ConversationHandler.END


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
    
