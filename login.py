from controle import limpar
import funcionario, controle
from banco_dados import *

def acessar(): #Realização do login do funcionário
    controle.limpar()

    validação = False
    usuario   = str(input('\nUsuário: '))
    senha     = str(input('Senha: '))
    validação = validar_login(usuario, senha)
    
    if validação == True:
        funcionario.main_func()
    else:
        print(" ERRO")

def validar_login(usuario, senha): #Validação de login do funcionário
    conta     = []
    conta     = login
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
            
            if   sair == 1:
                usuario = str(input('\nUsuário: '))
                senha   = str(input('Senha: '))
            elif sair == 2:
                return validação