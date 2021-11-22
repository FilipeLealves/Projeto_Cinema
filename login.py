from controle import validar_login
import funcionario

def acessar(): #Realização do login do funcionário
    validação = False
    usuario = str(input('Usuário: '))
    senha = str(input('Senha: '))

    validação = validar_login(usuario, senha)
    if validação == True:
        funcionario.main_func()
    else:
        return 0