from banco_dados import *
import os

#Onde o controle de cálculos serão feitos

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_filmes(num): #Listar os filmes
    lista = []
    if num == 1:
        lista = filmes_atual
    if num == 2:
        lista = filmes_breve

    for i in range(len(lista)):
        print(f'Nome: {lista[i][0]}\nDuração: {lista[i][1]}\nGênero: {lista[i][2]}\nSinopse: {lista[i][3]}\n')


def validar_login(usuario, senha): #Validação de login do funcionário
    conta = []
    conta = login
    validação = False

    while True:
        if conta[0] == usuario and conta[1] == senha:
            print('Login realizado com sucesso!')
            validação = True
            limpar()
            return validação
        else:
            limpar()
            print('\nLogin inválido!')
            sair = int(input('\n[1] - Tentar novamente\n[2] - Voltar\n\n>>> '))
            if sair == 1:
                usuario = str(input('\nUsuário: '))
                senha = str(input('Senha: '))
            elif sair == 2:
                return validação

def incluir_filmes(n,d,g,s):
    lista = [n,d,g,s]
    filmes_atual.append(lista)
    
