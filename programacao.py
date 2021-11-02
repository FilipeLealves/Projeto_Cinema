from controle import listar_filmes, limpar

#Todo o gerenciamento do banco de dados será feito aqui

def programacao():
    limpar()
    print('\n\tProgramação\n')
    listar_filmes(1) # Nº1 para FILMES ATUAIS | Nº2 para FILMES EM BREVE

programacao()