from banco_dados import *
import os

#Onde o controle de cálculos serão feitos

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_filmes(num): #Listar os filmes
    lista = ''
    i = 0
    valor = pega_valor()
    if num == 1:
        file = open('bd_atuais.txt','r')
        while i < valor:
            lista = file.readline()
            lista = lista.split(';')
            print(f'Nome: {lista[0]}\nDuração: {lista[1]}\nGênero: {lista[2]}\nSinopse: {lista[3]}\n')
            i+=1
    if num == 2:
        file = open('bd_novos.txt','r')
        while i < 2:
            lista = file.readline()
            lista = lista.split(';')
            print(f'Nome: {lista[0]}\nDuração: {lista[1]}\nGênero: {lista[2]}\nSinopse: {lista[3]}\n')
            i+=1

def pega_valor():
    file = open('bd_atuais.txt','r')
    cont = len(file.readlines())
    return cont
    close(file)

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
    file = open('bd_atuais.txt','a')
    x = ';'
    lista = [n,x,d,x,g,x,s,'\n']
    file.writelines(lista)
<<<<<<< HEAD
    print('giordano is so much gay')
=======
>>>>>>> 60892f69273ad0c4efc787748134b78c3e9914cf
