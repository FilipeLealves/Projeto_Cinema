import os, controle

RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
WHITE = "\033[1;37m"
PURPLE = "\033[1;35m"
BLACK = "\033[1;30m"
BLOCK = "\u2586"
FULL_BLOCK = "\u2588"
FULL_BLOCK += WHITE

UPLINE = '\u2594'

OO = GREEN+BLOCK*2+' '
XX = RED+BLOCK*2+' '

sala = [[OO,OO,OO,OO,OO,OO,OO,OO,OO,OO],
        [OO,OO,OO,OO,OO,OO,OO,OO,OO,OO],
        [OO,OO,OO,OO,OO,OO,OO,OO,OO,OO],
        [OO,OO,OO,OO,OO,OO,OO,OO,OO,OO],
        [OO,OO,OO,OO,OO,OO,OO,OO,OO,OO],
        [OO,OO,OO,OO,OO,OO,OO,OO,OO,OO],
        [OO,OO,OO,OO,OO,OO,OO,OO,OO,OO],
        [OO,OO,OO,OO,OO,OO,OO,OO,OO,OO],
        [OO,OO,OO,OO,OO,OO,OO,OO,OO,OO],
        [OO,OO,OO,OO,OO,OO,OO,OO,OO,OO],]

alpha  = []
num    = []
result = []
n1 = 0
n2 = 0
cadeiras = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sessao(code):
    global sala, alpha, num, result, n1, n2, cadeiras

    valor = controle.pega_valor_2()

    file  = open('bd_sessoes.txt','r')
    i     = 0
    lista = ''
    
    while i < code + 1:
        lista = file.readline()
        lista = lista.split(';')
        filme = lista[0]
        this_sessao = lista[1]
        i += 1

    #print(f'Filme: {filme} | Sesssão: {this_sessao} | Code: {code}')

    ok = True
    cadeiras_escolhidas = 0
    lugar_lista = ([''])
    valor_inteira = 32
    valor_meia = 16
    valor_total = 0
    pagar = 0

    while True:
        clear()
        print(RED+'\t       {}'.format(filme))
        print(f'\t       {this_sessao}\n')
        print(CYAN+'\t   1  2  3  4  5  6  7  8  9  10')
        
        for i in range(len(sala)):
            print(CYAN+f'\t{chr(65+i)}  '+sala[0][i]+sala[1][i]+sala[2][i]+sala[3][i]+sala[4][i]+sala[5][i]+sala[6][i]+sala[7][i]+sala[8][i]+sala[9][i])
        
        print(WHITE+'\t   _____________________________')
        print('\t   '+FULL_BLOCK*4+' T '+FULL_BLOCK*3+' E '+FULL_BLOCK*3+' L '+FULL_BLOCK*3+' A '+FULL_BLOCK*4)
        print('\t   '+UPLINE*29)

        escolha_sim = ['sim','Sim','SIM','s','S']
        escolha_nao = ['não','Não','NÃO','n','N','nao']

        if ok == False:
            i = 1
            while i <= cadeiras_escolhidas:
                print(f'\t    Cadeira selecionada: {lugar_lista[i]}')
                i+=1
            print('\t    Valor de ingressos:\n\t    Inteiro - R$ 32,00\n\t    Meia-entrada - R$ 16,00\n')
            escolha = input('\n\t    Deseja comprar ingressos meia-entrada? [sim] / [não]\n\n>>> ')

            if escolha in escolha_sim:
                total_meia = int(input('\t    Total de meia-entradas que serão compradas: '))
                total_inteira = cadeiras_escolhidas - total_meia
                valor_total = (total_inteira * valor_inteira) + (total_meia * valor_meia)
            if escolha in escolha_nao:
                valor_total = cadeiras_escolhidas * valor_inteira

            print(f'\t    Valor total a ser pago: R${valor_total},00')
            forma_pagamento = int(input('\n\t    Qual método de pagamento | 1 - Cartão / 2 - Dinheiro'))

            if forma_pagamento == 1:
                final = int(input('\n\t    Finalizar compra? | 1 - Sim / 2 - Não'))
                if final == 1:
                    print('\n\t    Compra finalizada com sucesso!')
                    print(f'\n\t    Nome do filme: {filme}\nSessão: {this_sessao}\nCadeiras: {lugar_lista}')
                else:
                    return 0
                input('')
            elif forma_pagamento == 2:
                pagar = float(input('\n\t    Digite quanto deseja pagar: '))

                if pagar < valor_total:
                    while pagar < valor_total:
                        valor = valor_total - pagar
                        print(f'\n\t    Valor insuficiente! Falta R$ {valor},00')
                        pagar = float(input('\n\t    Digite quanto deseja pagar: '))

                elif pagar == valor_total:
                    print('\n\t    Compra finalizada com sucesso!')
                    print(f'\n\t    Nome do filme: {filme}\nSessão: {this_sessao}\nCadeiras: {lugar_lista}')

                elif pagar > valor_total:
                    valor = pagar - valor_total
                    print(f'\n\t    Compra finalizada com sucesso! | R$ {valor},00 de troco')
                    print(f'\n\t    Nome do filme: {filme}\nSessão: {this_sessao}\nCadeiras: {lugar_lista}')
                
                input('')

        if  cadeiras == 0 and ok:
            cadeiras = int(input('\tQuantas cadeiras: '))
            cadeiras_escolhidas = cadeiras

        elif cadeiras > 0:
            print(f'\tCadeiras: {cadeiras}')
            print(WHITE+'\n\tQual lugar deseja marcar?\n')
            lugar = str(input('\t>>> ').upper())
            lugar_lista.append(lugar)
            cadeiras -= 1

            if cadeiras == 0:
                ok = False

            for item in lugar:
                if item.isdigit():
                    num.append(item)
                else:
                    alpha.append(item)

            result = [''.join(num)]
            num.clear()
            num = list(map(int,result))
            n1  = num[0]

            letra = alpha[0]

            if   letra == 'A':
                n2 = 1
            elif letra == 'B':
                n2 = 2
            elif letra == 'C':
                n2 = 3
            elif letra == 'D':
                n2 = 4
            elif letra == 'E':
                n2 = 5
            elif letra == 'F':
                n2 = 6
            elif letra == 'G':
                n2 = 7
            elif letra == 'H':
                n2 = 8
            elif letra == 'I':
                n2 = 9
            elif letra == 'J':
                n2 = 10

            if sala[int(n1)-1][n2-1] == OO:
                sala[int(n1)-1][n2-1] = XX
            else:
                print('Lugar já está ocupado!')
            
            num.clear()
            alpha.clear()

            controle.limpar()
