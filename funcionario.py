from controle import incluir_filmes, listar_filmes, limpar
from banco_dados import *

def main():
    while True:
        print('\n')
        print('\tMenu')
        print('\n[1] - Cadastro de filme\n[2] - Listar filmes\n[3] - Cadastrar sessões\n[0] - Sair\n')

        x = menu(int(input('>>> ')))

        if x == False:
            break

def menu(x):
    limpar()
    if x == 1:
        cadastro_filmes()
    elif x == 2:
        filmes_listados()
    elif x == 3:
        cadastrar_sessao()
    elif x == 0:
        return False

def cadastro_filmes():
    print('Cadastro de filme\n')
    nome = str(input('Nome: '))
    duração = str(input('Duração: '))
    genero = str(input('Gênero: '))
    sinopse = str(input('Sinopse: '))

    incluir_filmes(nome,duração,genero,sinopse)

def filmes_listados():
    listar_filmes(1)

def cadastrar_sessao():
    file = open('bd_atuais.txt','r')
    lista = file.readline()
    lista = lista.split(';')

    for i in range(len(lista)):
        print(f'Filme nº{i + 1}: {lista[0]}')
        sessoes.append(lista[0])
    
    var = True

    for i in range(len(filmes_atual)):
            sessoes.append([filmes_atual[i][0]])

    while var:
        for i in range(len(filmes_atual)):
            print(f'Filme {i + 1}: {filmes_atual[i][0]}')
            

        escolha = (int(input("\nDeseja adicionar sessão para qual filme?\n>>> ")))

        if escolha == 1:
            sessao = input("\nDigite o número da sala e o horário da sessão...\n(Exemplo - Sala 1 - 10h30)\n\nDigite >>> ")

main()