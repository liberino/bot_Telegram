#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileWriter, PdfFileReader

checklists_manutencao= {
    "Balão":  open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Guincho":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Gondola":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Cabo de ancoragem":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Caixa de dados":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Caixa do guincho":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Berço de solo":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Berço da pizza/picape":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb')
    
    
}

url_manutencao = {
    "Balão": 'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Guincho": 'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Gondola":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Cabo de ancoragem":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Caixa de dados":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Caixa do guincho":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Berço de solo":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Berço da pizza/picape":  'https://www.youtube.com/watch?v=7dKQWw96kcM'
    
    }
