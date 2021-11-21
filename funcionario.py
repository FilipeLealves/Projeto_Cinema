from controle import incluir_filmes, listar_filmes, limpar
from banco_dados import *

def main():
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
    
    var = True

    for i in range(len(filmes_atual)):
            sessoes.append([filmes_atual[i][0]])

    while var:
        for i in range(len(filmes_atual)):
            print(f'Filme {i + 1}: {filmes_atual[i][0]}')
            

        escolha = (int(input("\nDeseja adicionar sessão para qual filme?\n>>> ")))

        opcoes = [1, 2, 3, 4, 5, 6]

        for j in opcoes:
            if escolha == j:
                i = escolha - 1
            
                sessao = input("\nDigite o número da sessão e o horario da sessão...\n(Exemplo - Sessão 1 - 10h30)\n\nDigite >>> ")
                sessoes[i].append(sessao)

                print(sessoes)
                
                """print(f"Filme: {sessoes[i][0]}")

                for c in range(1, (len(sessoes))):
                    print(c)
                    print(f"Sessões: {sessoes[i][c]}")"""

                continuar = input("\nDeseja continuar adicionando sessão para algum filme?\nDigite 'Sim' ou 'Não' para continuar\n>>> ")

                if continuar == "Não" or continuar == "não":
                    var = False

main()