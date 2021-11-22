from controle import incluir_filmes, listar_filmes, limpar, pega_valor
from banco_dados import *
import random

def main_func():
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
    
    lista = ''
    valor = pega_valor()
    file = open('bd_atuais.txt','r')
    i = 0

    while i < valor:
        lista = file.readline()
        lista = lista.split(';')
        print(f'Filme nº{i + 1}: {lista[0]}')
        i += 1
            
    escolha = (int(input("\nDeseja adicionar sessão para qual filme?\n>>> ")))

    i = 0
    
    lista = ''
    valor = pega_valor()
    file = open('bd_atuais.txt','r')
    
    while i < escolha:
        num = random.randint(1,20)
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