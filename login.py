from controle import validar_login
from funcionario import main

def acessar(): #Realização do login do funcionário
    validação = False
    usuario = str(input('Usuário: '))
    senha = str(input('Senha: '))

    validação = validar_login(usuario, senha)
    if validação == True:
        main()
    else:
        return 0
acessar()