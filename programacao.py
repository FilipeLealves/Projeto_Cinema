from controle import listar_filmes, limpar, listar_sessoes, comprar_ingresso

#Todo o gerenciamento do banco de dados será feito aqui

def programacao():
    limpar()
    while True:     
        print('\n\tProgramação\n')
        print('Para ver a nossa programação de filmes é só escolher uma das opções abaixo...\n\n1 - Filmes atuais\n2 - Filmes breve\n3 - Ver sessões\n\n0 - Voltar\n')

        x = (int(input('Digite a opção desejada: ')))
        print('\n')

        if   x == 1:
            listar_filmes(1) # Nº1 para FILMES ATUAIS | Nº2 para FILMES EM BREVE
        elif x == 2:
            listar_filmes(2) # Nº1 para FILMES ATUAIS | Nº2 para FILMES EM BREVE
        elif x == 3:
            listar_sessoes()
            comprar_ingresso()
        elif x == 0:
            break