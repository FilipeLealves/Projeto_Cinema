import banco_dados, controle, funcionario, programacao
#Módulo principal onde o programa vai rodar

def main():
    while True:
        print('\n')
        print('\tCinema Uniesp')
        print('Bem-vindo ao Cinema Uniesp!\n\nMenu:\n1 - Programação\n')

        escolha = (int(input('Digite o número da opção que deseja acessar >>> ')))

        if   escolha == 1:
            programacao.programacao()
        elif escolha == 0:
            break

main()