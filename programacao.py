import controle

#Todo o gerenciamento do banco de dados será feito aqui

class Poo():

    def variavel(self):
        self.x = 3
        self.y = 7

def printar():
    p = Poo()
    p.variavel()
    print(p.x,p.y)

def programacao():
    while True:
        controle.limpar() 
        print('\n\tProgramação\n')
        print('Para ver a nossa programação de filmes é só escolher uma das opções abaixo...\n\n1 - Filmes atuais\n2 - Filmes breve\n3 - Ver sessões\n\n0 - Voltar\n')

        escolha = (int(input('Digite a opção desejada: ')))
        print('\n')

        if   escolha == 1:
            controle.listar_filmes(1) # Nº1 para FILMES ATUAIS | Nº2 para FILMES EM BREVE
        elif escolha == 2:
            controle.listar_filmes(2) # Nº1 para FILMES ATUAIS | Nº2 para FILMES EM BREVE
        elif escolha == 3:
            controle.listar_sessoes()
            controle.comprar_ingresso()
        elif escolha == 0:
            break