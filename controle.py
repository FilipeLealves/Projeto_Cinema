from banco_dados import *
import os

from sessao import sessoes

#Onde o controle de cálculos serão feitos

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_filmes(num): #Listar os filmes
    limpar()
    
    lista = ''
    i     = 0
    valor = pega_valor()
    valor_novos = pega_novos()
    
    if num == 1:
        file = open('bd_atuais.txt','r')

        if valor > 0:
            while i < valor:
                lista = file.readline()
                lista = lista.split(';')
                print(f'Nome: {lista[0]}\nDuração: {lista[1]}\nGênero: {lista[2]}\nSinopse: {lista[3]}\n')
                i += 1
        else:
            print("\nErro! Nenhum filme foi cadastrado no momento!")
        
        input("\nAperte enter para continuar...")

    if num == 2:
        file = open('bd_novos.txt','r')
        
        if valor_novos > 0:
            while i < valor_novos:
                lista = file.readline()
                lista = lista.split(';')
                print(f'Nome: {lista[0]}\nDuração: {lista[1]}\nGênero: {lista[2]}\nSinopse: {lista[3]}\n')
                i += 1
        else:
            print("\nErro! Nenhum filme foi cadastrado no momento!")

        input("\nAperte enter para continuar...")

def comprar_ingresso():
    escolha     = input('\nDeseja comprar ingresso?\n>>> ')
    lista = ['sim','Sim','SIM','s','S','1','sIM']
    num   = [0,1,2,3,4,5,6,7,8,9,10]
    
    if escolha in lista:
        code = input('\nCódigo da sessão: ')
        right_code = verificar_code(code)
        
        if  right_code == 9999:
            print('\nCódigo inválido ou inexistente!')
        elif right_code in num:
            sessoes(right_code)
    else:
        pass

def verificar_code(code):
    code  = code + '\n'
    file  = open('bd_sessoes.txt','r')
    valor = pega_valor_2()
    i     = 0
    lista = []
    
    while i < valor:
        this = file.readline()
        this = this.split(';')
        lista.append(this[2])
        i += 1
    
    j = 0
    
    while j < valor:
        if lista[j] == code:
            return j
        else:
            pass
        
        j += 1
    return 9999

def listar_sessoes():
    limpar()
    file  = open('bd_sessoes.txt','r')
    count = pega_valor_2()
    i     = 0
    lista = ''
    
    while i < count:
        lista = file.readline()
        lista = lista.split(';')
        print(f'Filme: {lista[0]}\nSessão: {lista[1]}\nCódigo: {lista[2]}\n')
        i += 1

def pega_valor():
    file = open('bd_atuais.txt','r')
    cont = len(file.readlines())
    return cont
    close(file)

def pega_novos():
    file = open('bd_novos.txt','r')
    cont = len(file.readlines())
    return cont
    close(file)

def pega_valor_2():
    file = open('bd_sessoes.txt','r')
    cont = len(file.readlines())
    return cont

def incluir_filmes(n,d,g,s):
    file  = open('bd_atuais.txt','a')
    x     = ';'
    lista = [n,x,d,x,g,x,s,'\n']
    file.writelines(lista)

def incluir_breves(n,d,g,s):
    file  = open('bd_novos.txt','a')
    x     = ';'
    lista = [n,x,d,x,g,x,s,'\n']
    file.writelines(lista)