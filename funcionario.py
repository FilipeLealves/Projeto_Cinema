from controle import *
from banco_dados import *
import random

def main_func():
    while True:
        limpar()

        print('\n')
        print('\tMenu')
        print('\n1 - Cadastro de filme\n2 - Cadastro de filmes em breve\n3 - Listar filmes\n4 - Cadastrar sessões\n\n0 - Sair\n')

        x = menu(int(input('>>> ')))

        if x == False:
            break

def menu(x):
    limpar()
    
    if   x == 1:
        cadastro_filmes()
    elif x == 2:
        cadastro_breves()
    elif x == 3:
        filmes_listados()
    elif x == 4:
        cadastrar_sessao()
    elif x == 0:
        return False

def cadastro_filmes():
    limpar()

    print('Cadastro de filme\n')
    nome    = str(input('Nome: '))
    duração = str(input('Duração: '))
    genero  = str(input('Gênero: '))
    sinopse = str(input('Sinopse: '))

    incluir_filmes(nome,duração,genero,sinopse)

def cadastro_breves():
    limpar()

    print('Cadastro de filme\n')
    nome    = str(input('Nome: '))
    duração = str(input('Duração: '))
    genero  = str(input('Gênero: '))
    sinopse = str(input('Sinopse: '))

    incluir_breves(nome,duração,genero,sinopse)

def filmes_listados():
    limpar()

    escolha = int(input("Deseja visualizar quais filmes...\n\n1 - Filmes atuais\n2 - Filmes em breve\n\n>>> "))
    listar_filmes(escolha)

def cadastrar_sessao():
    limpar()

    lista = ''
    valor = pega_valor()
    file  = open('bd_atuais.txt','r')
    i     = 0

    while i < valor:
        lista = file.readline()
        lista = lista.split(';')
        print(f'Filme nº{i + 1}: {lista[0]}')
        i += 1
            
    escolha = (int(input("\nDeseja adicionar sessão para qual filme?\n>>> ")))

    i = 0
    
    lista = ''
    valor = pega_valor()
    file  = open('bd_atuais.txt','r')
    
    while i < escolha:
        num   = random.randint(1,20)
        num_char = random.randint(65,90)
        lista = file.readline()
        lista = lista.split(';')
        filme = lista[0]
        i += 1

    code = chr(num_char) + str(num)
    file = open('bd_sessoes.txt','a')

    sessao = input("\nDigite o número da sala e o horário da sessão...\n(Exemplo - Sala 1 - 10h30)\n\n>>> ")

    filme = filme + ';' + sessao + ';' + code +'\n' 
    file.writelines(filme)