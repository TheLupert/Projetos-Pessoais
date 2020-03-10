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
    nome_aniv = input("Digite o nome do novo aniversáriante:")
    #if nome_aniv == "cancel" or "Cancel"
    while nome_aniv in aniversários:
        nome_aniv = input("Aniversariante já existente no banco de dados. Por favor, complemente o nome ou use outro:")
    data_aniv = str(input("Agora, digite a data de aniversário da pessoa no formato DD/MM/AAAA:"))
    dataRegex = r'\d{2}/\d{2}/\d{4}'
    matchAniv = re.search(dataRegex, str(data_aniv))
    while matchAniv == None:
        data_aniv = input("Data inválida, tente novamente:")
        dataRegex = r'\d{2}/\d{2}/\d{4}'
        matchAniv = re.search(dataRegex, str(data_aniv))
    aniversários[nome_aniv] = data_aniv
    print("Aniversáriante adicionado com sucesso!")
elif cmd == 'Edit' or 'edit':
    aniv_edit = input("Digite o nome do aniversáriante:")
    if aniv_edit in aniversários:
        print('''O que deseja mudar?
        Digite 'Nome' para mudar nome da pessoa.
        Digite 'Data' para mudar o aniversário da pessoa.''')
        mudanca = str(input("Digite aqui sua opção:"))
        if mudanca == 'Nome' or 'nome':
            novo_nome = input("Digite o novo nome:")
            aniversários[novo_nome] = aniversários.pop(aniv_edit)
            print("Nome mudado com sucesso!")
        elif mudanca == 'Data' or 'data':
            nova_data = input("Digite a nova data de aniversário:")
            aniversários[aniv_edit] = nova_data
            print("Aniversário atualizado com sucesso!")
        else:
            print("Comando inválido, tente novamente!")
            mudanca = input("O que deseja mudar?")
    else:
        print("Aniversariante não existe nos registros. Tente novamente ou deixe em branco para voltar.")
        aniv_edit = input("Digite o nome do aniversáriante:")
elif cmd == 'Remove' or 'remove':
    aniv_remov = input("Digite o nome do aniversáriante a ser removido:")
    if aniv_remov in aniversários:
        aniversários.pop("aniv_remov")
    else:
        print("Aniversário não existente no dicionário. Tente novamente.")
        aniv_remov = input("Digite o nome do aniversáriante a ser removido:")

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

