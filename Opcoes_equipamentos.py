#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileWriter, PdfFileReader

Tutoriais= {
#Balao
    'Abastecimento':  open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Transfusão':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Teste da Baliza':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Reparo no PU':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Reparo no Nylon':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Troca do cartucho da deflação':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Outros_Balão':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
#Guincho
    'Manual de montagem_Guincho':  open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Teste elétrico_Guincho':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Manual de manutenção mensal_Guincho':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Manual de manutenção semestral_Guincho':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Outros_Guincho':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
#Gondola
    'Teste da deflação':  open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Pareamento do PLC':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Teste do SPOT':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Verificação da conexão (PING)':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Diagrama elétrico_Gondola':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Manual de montagem_Gondola':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Outros_Gondola':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
#Cabo_de_ancoragem
    'Reparo do conector_Cabo de Ancoragem':  open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Reparo do stopper':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Outros_Cabo de Ancoragem':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
#Caixa_de_dados
    #'Pareamento do PLC':  open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Manual de montagem_Caixa de dados':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Diagrama elétrico_Caixa de dados':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Outros_Caixa de dados':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
#Caixa_do_guincho
    'Manual de montagem_Caixa do guincho':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Diagrama elétrico_Caixa do guincho':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Outros_Caixa do guincho':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
#Berco_de_solo
    'Instalação de ancoras':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Manual de montagem_Berço de solo':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Outros_Berço de solo':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    
    'Picapes compatíveis':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Manual de montagem_Berço da pizza/picape':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    'Outros_Berço da pizza/picape':   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),

}

url_tutoriais= {
#Balao
    'Abastecimento':  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Transfusão':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Teste da Baliza':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Reparo no PU':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Reparo no Nylon':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Troca do cartucho da deflação':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Outros_Balão':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
#Guincho 
    'Manual de montagem_Guincho':  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Teste elétrico_Guincho':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Manual de manutenção mensal_Guincho':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Manual de manutenção semestral_Guincho':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Outros_Guincho':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
#Gondola
    'Teste da deflação':  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    #'Pareamento do PLC':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Teste do SPOT':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Verificação da conexão (PING)':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Diagrama elétrico_Gondola':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Manual de montagem_Gondola':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Outros_Gondola':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
#Cabo_de_ancoragem 
    'Reparo do conector_Cabo de Ancoragem':  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Reparo do stopper':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Outros_Cabo de Ancoragem':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
#Caixa_de_dados
    'Pareamento do PLC':  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Manual de montagem_Caixa de dados':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Diagrama elétrico_Caixa de dados':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Outros_Caixa de dados':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
#Caixa_do_guincho
    'Manual de montagem_Caixa do guincho':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Diagrama elétrico_Caixa do guincho':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Outros_Caixa do guincho':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
#Berco_de_solo
    'Instalação de ancoras':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Manual de montagem_Berço de solo':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Outros_Berço de solo':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    
    'Picapes compatíveis':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Manual de montagem_Berço da pizza/picape':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    'Outros_Berço da pizza/picape':   'https://www.youtube.com/watch?v=7dKQWw96kcM',
    
}