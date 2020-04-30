#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileWriter, PdfFileReader

switcher= {
    "Acesso Sauron":  open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Streaming Sauron":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Tutorial Completo Sauron":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Acusar erro Sauron":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Outros tutoriais Sauron":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Credenciais Sauron":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Link de acesso Sauron":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Debug Sauron":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Adicionar tutorial Sauron":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    
    "Acesso Harpia":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Streaming Harpia":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Tutorial Completo Harpia":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Acusar erro Harpia":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Outros tutoriais Harpia":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Credenciais Harpia":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Link de acesso Harpia":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Debug Harpia":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Adicionar tutorial Harpia":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    
    "Acesso Tupan":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Streaming Tupan":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Tutorial Completo Tupan":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Acusar erro Tupan":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Outros tutoriais Tupan":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Credenciais Tupan":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Link de acesso Tupan":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Debug Tupan":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Adicionar tutorial Tupan":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    
    "Acesso Geocam":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Streaming Geocam":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Tutorial Completo Geocam":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Acusar erro Geocam":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Outros tutoriais Geocam":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Credenciais Geocam":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Link de acesso Geocam":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Debug Geocam":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb'),
    "Adicionar tutorial Geocam":   open('7__PLANO_DE_NEG_CIOS___RBQ___PIPE_Fase_2.pdf','rb')
    
}

url = {
    "Acesso Sauron": 'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Streaming Sauron": 'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Tutorial Completo Sauron":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Acusar_Erro Sauron":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Outros_tutoriais Sauron":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Credenciais Sauron":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Link de acesso Sauron":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Debug Sauron":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Adicionar tutorial Sauron":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    
    "Acesso Harpia":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Streaming Harpia":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Tutorial Completo Harpia":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Acusar_Erro Harpia":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Outros_tutoriais Harpia":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Credenciais Harpia":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Link de acesso Harpia":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Debug Harpia":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Adicionar tutorial Harpia":'https://www.youtube.com/watch?v=7dKQWw96kcM',
    
    "Acesso Tupan":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Streaming Tupan":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Tutorial Completo Tupan":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Acusar_Erro Tupan":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Outros_tutoriais Tupan":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Credenciais Tupan":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Link de acesso Tupan":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Debug Tupan":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Adicionar tutorial Tupan": 'https://www.youtube.com/watch?v=7dKQWw96kcM',
    
    "Acesso Geocam":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Streaming Geocam":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Tutorial Completo Geocam":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Acusar_Erro Geocam":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Outros_tutoriais Geocam":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Credenciais Geocam":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Link de acesso Geocam":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Debug Geocam":  'https://www.youtube.com/watch?v=7dKQWw96kcM',
    "Adicionar tutorial Geocam": 'https://www.youtube.com/watch?v=7dKQWw96kcM'
    }
