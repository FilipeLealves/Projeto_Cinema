from controle import incluir_filmes, listar_filmes, limpar

def main():
    while True:
        print('\tMenu')
        print('\n[1] - Cadastro de filme\n[2] - Listar filmes\n[0] - Sair\n')

        x = menu(int(input('>>> ')))

def menu(x):
    limpar()
    if x == 1:
        cadastro_filmes()
    elif x == 2:
        filmes_listados()
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
