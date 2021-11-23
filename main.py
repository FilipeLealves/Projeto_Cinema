import banco_dados, controle, funcionario, programacao, login
#Módulo principal onde o programa vai rodar

def main():
    while True:
        controle.limpar()

        print('\n')
        print('\tCinema Uniesp')
        print('Bem-vindo ao Cinema Uniesp!\n\nMenu:\n\n1 - Programação\n2 - Login\n\n0 - Sair \n')

        escolha = (int(input('>>> ')))

        if   escolha == 1:
            programacao.programacao()
        elif escolha == 2:
            login.acessar()
        elif escolha == 0:
            break

main() 