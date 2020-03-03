#-------------------------------------------------------------------------------
# Name:        Birthday Memorizer
# Purpose:
#
# Author:      Usuário
#
# Created:     07/02/2020
# Copyright:   (c) Usuário 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
aniversários = {}
import re

print('Olá! O que deseja fazer?')
print('''Digite algo da seguinte lista de opções:
    'Add' para adicionar novo aniversáriante.
    'Edit' para editar um aniversariante.
    'Remove' para excluir um aniversariante da lista.
    'List' para ver todos os aniversariantes catalogados.
    'Exit' para sair do programa.''')

cmd = input("Digite aqui seu comando:")

if cmd == 'add' or 'Add':
    nome_aniv = input("Digite o nome do aniversáriante:")
    while nome_aniv in aniversários:
        nome_aniv = input("Aniversariante já existente no banco de dados. Por favor, complemente o nome ou use outro:")
    data_aniv = str(input("Agora, digite a data de aniversário da pessoa no formato DD/MM/AAAA:"))
    aniversários[nome_aniv] = data_aniv
    dataRegex = r'\d{2}/\d{2}/\d{4}'
    matchAniv = re.search(dataRegex, str(data_aniv))
    while matchAniv == None:
        data_aniv = input("Data inválida, tente novamente:")
        dataRegex = r'\d{2}/\d{2}/\d{4}'
        matchAniv = re.search(dataRegex, str(data_aniv))
    if nome_aniv in aniversários:
        print("Aniversáriante adicionado com sucesso!")
##elif cmd == 'Edit' or 'edit':
##
##elif cmd == 'Remove' or 'remove':
##
##elif cmd == 'List' or 'list':
##
##elif cmd == 'Exit' or 'exit':
##
##else:
##    return print('Comando inválido, tente novamente.')
##
##
##
##
##
##
##
##birthdays = []
##
##def novoaniversário(nome,data):
##    nome = input("Por favor, coloque o nome do aniversariante:")
##
##    data = input("Agora, coloque a data de aniversário da pessoa:")

