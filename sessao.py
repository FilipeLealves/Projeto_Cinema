import os

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

alpha = []
num = []
result = []
n1 = 0
n2 = 0
cadeiras = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print(CYAN+'\t   1  2  3  4  5  6  7  8  9  10')
    for i in range(len(sala)):
        print(CYAN+f'\t{chr(65+i)}  '+sala[0][i]+sala[1][i]+sala[2][i]+sala[3][i]+sala[4][i]+sala[5][i]+sala[6][i]+sala[7][i]+sala[8][i]+sala[9][i])
    print(WHITE+'\t   _____________________________')
    print('\t   '+FULL_BLOCK*4+' T '+FULL_BLOCK*3+' E '+FULL_BLOCK*3+' L '+FULL_BLOCK*3+' A '+FULL_BLOCK*4)
    print('\t   '+UPLINE*29)
    if cadeiras == 0:
        cadeiras = int(input('\tQuantas cadeiras: '))
    elif cadeiras > 0:
        print(f'\tCadeiras: {cadeiras}')
        print(WHITE+'\n\tQual lugar deseja marcar?\n')
        lugar = str(input('\t>>> ').upper())
        cadeiras-=1

        for item in lugar:
            if item.isdigit():
                num.append(item)
            else:
                alpha.append(item)

        result = [''.join(num)]
        num.clear()
        num = list(map(int,result))
        n1 = num[0]

        letra = alpha[0]

        if letra == 'A':
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
            print('Lugar já esta ocupado!')
        
        num.clear()
        alpha.clear()
