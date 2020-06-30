#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lupert
#
# Created:     15/06/2020
# Copyright:   (c) Lupert 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re

aniversarios = {"Gabriel":"17/11/1994"}
comandos = ("Add", "add", "Edit", "edit", "Remove", "remove", "List", "list", "Exit", "exit")
# Programar algo que impessa o usuário de deixar campos em branco.

while True:
    print('O que deseja fazer?')
    print('''Digite algo da seguinte lista de opções:
    'Add' para adicionar novo aniversáriante.
    'Edit' para editar um aniversariante.
    'Remove' para excluir um aniversariante da lista.
    'List' para ver todos os aniversariantes catalogados.
    'Exit' para sair do programa.''')
    cmd = input("Digite aqui seu comando:")
    while cmd not in comandos:
        print("Comando inválido, tente novamente!")
        cmd = input("Digite aqui seu comando:")
    if cmd == "Add" or cmd == "add": #Adicionar pessoas na lista.
        nome_aniv = str(input("Digite o nome do novo aniversáriante. Deixe em branco para voltar."))
        if nome_aniv != "":
            while nome_aniv in aniversarios:
                nome_aniv = input("Aniversariante já existente no banco de dados. Por favor, complemente o nome ou use outro:")
            data_aniv = str(input("Agora, digite a data de aniversário da pessoa no formato DD/MM:"))
            dataRegex = re.compile(r'(\d{2}/\d{2})(/\d{4})?')
            matchAniv = re.search(dataRegex, str(data_aniv))
            while matchAniv == None:
                data_aniv = str(input("Data inválida, tente novamente:"))
                dataRegex = re.compile(r'(\d{2}/\d{2})(/\d{4})?')
                matchAniv = re.search(dataRegex, str(data_aniv))
            aniversarios[nome_aniv] = data_aniv
            print("Aniversáriante adicionado com sucesso!")
    elif cmd == 'Edit' or cmd == 'edit': #Editar contatos.
        aniv_edit = str(input("Digite o nome do aniversáriante. Deixe em branco para voltar."))
        if aniv_edit != "":
            while aniv_edit not in aniversarios: #Verificar se aniversariante está no arquivo.
                print("Aniversariante não existe nos registros. Tente novamente.")
                aniv_edit = str(input("Digite o nome do aniversáriante:"))
            print('''O que deseja mudar?
                Digite 'Nome' para mudar nome da pessoa.
                Digite 'Data' para mudar o aniversário da pessoa.
                Deixe em branco para voltar.''')
            while True:
                mudanca = str(input("Digite aqui sua opção:"))
                opcaoEdit = ("Nome","nome","Data","data","")
                while mudanca not in opcaoEdit: #Evita que o usuário digite comandos errados.
                    print('''O que deseja mudar?
                Digite 'Nome' para mudar nome da pessoa.
                Digite 'Data' para mudar o aniversário da pessoa.
                Deixe em branco para voltar.''')
                    mudanca = str(input("O que deseja mudar?"))
                if mudanca == 'Nome' or mudanca == 'nome':
                    novo_nome = str(input("Digite o novo nome:"))
                    while novo_nome == "":
                        print("Nome em branco, tente novamente!")
                        novo_nome = str(input("Digite o novo nome:"))
                    aniversarios[novo_nome] = aniversarios.pop(aniv_edit)
                    print("Nome mudado com sucesso!")
                elif mudanca == "Data" or mudanca == "data":
                    nova_data = str(input("Digite a nova data de aniversário:"))
                    dataRegex = re.compile(r'(\d{2}/\d{2})(/\d{4})?')
                    matchAniv = re.search(dataRegex, str(data_aniv))
                    while matchAniv == None:
                        data_aniv = str(input("Data inválida, tente novamente:"))
                        dataRegex = re.compile(r'(\d{2}/\d{2})(/\d{4})?')
                        matchAniv = re.search(dataRegex, str(data_aniv))
                    aniversarios[aniv_edit] = nova_data
                    print("Aniversário atualizado com sucesso!")
                else:
                    break
    elif cmd == "Remove" or cmd == "remove": #Remover aniversariante.
        aniv_remov = str(input("Digite o aniversáriante a ser removido:"))
        while aniv_remov not in aniversarios:
            print("Aniversariante não existe nos registros. Tente novamente ou deixe em branco para voltar.")
            aniv_remov = str(input("Digite o aniversáriante a ser removido:"))
        if aniv_remov != "":
            aniversarios.pop(aniv_remov)
            print("Aniversáriante removido com sucesso!")
    elif cmd == "List" or cmd == "list":
        for x,y in aniversarios.items():
            print("Nome: "+x+" / Aniversário: "+y) #Será que tem como fazer isso aparecer em um popup? Ou algo separado?
    else:
        break