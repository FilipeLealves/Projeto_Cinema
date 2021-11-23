from controle import limpar, validar_login
import funcionario, controle

def acessar(): #Realização do login do funcionário
    controle.limpar()

    validação = False
    usuario   = str(input('\nUsuário: '))
    senha     = str(input('Senha: '))
    validação = validar_login(usuario, senha)
    
    if validação == True:
        funcionario.main_func()
    else:
        return 0