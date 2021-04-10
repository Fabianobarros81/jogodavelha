from random import randrange
from os import system, name
from time import sleep

p = []
final = int(1)
coluna = linha = int(0)

for i in range(1, 5):
    p.append([' '] * 4)


def jogada(cjogada, ljogada, jogador):
    if p[cjogada][ljogada] in 'XO':
        return False
    else:
        p[cjogada][ljogada] = jogador
        return True


def mostratela():
    system('cls' if name == 'nt' else 'clear')

    print('\033[1;34m\n\n')
    print(f'        C1  C2  C3  \n')
    print(f'   L1   {p[1][1]} | {p[2][1]} | {p[3][1]}')
    print(f'       -----------')
    print(f'   L2   {p[1][2]} | {p[2][2]} | {p[3][2]}')
    print(f'       -----------')
    print(f'   L3   {p[1][3]} | {p[2][3]} | {p[3][3]}')
    print('\n')


def validavencedor():
    valida = ''
    for x in range(1, 4):
        if len(valida) != 4:
            valida = ''
            for y in range(1, 4):
                if p[x][y] != ' ':
                    valida = valida + p[x][y]
                if valida == 'XXX' or valida == 'OOO':
                    valida = valida + p[x][y]

    for x in range(1, 4):
        if len(valida) != 4:
            valida = ''
            for y in range(1, 4):
                if p[y][x] != ' ':
                    valida = valida + p[y][x]
                if valida == 'XXX' or valida == 'OOO':
                    valida = valida + p[y][x]

    if len(valida) != 4:
        valida = ''
        for a in range(1, 4):
            if p[a][a] != ' ':
                valida = valida + p[a][a]
                if valida == 'XXX' or valida == 'OOO':
                    valida = valida + p[0][0]

    if len(valida) != 4:
        valida = ''
        c = 3
        for b in range(1, 4):
            if p[b][c] != ' ':
                valida = valida + p[b][c]
            if valida == 'XXX' or valida == 'OOO':
                valida = valida + p[0][0]
            c = c - 1

    if len(valida) == 4:
        vencedor = valida[0]
        print(f'\033[0;33m O VENCEDOR FOI: {vencedor}')
        exit(0)


while not final == 6:
    mostratela()
    validavencedor()

    while True:
        coluna = int(input('\033[0;32mDigite uma coluna [1 a 3]: '))
        if 0 <= coluna <= 3:
            break

    while True:
        linha = int(input('\033[0;32mDigite uma linha [1 a 3]: '))
        if 0 <= linha <= 3:
            break

    resp = jogada(coluna, linha, 'X')
    while not resp:
        print(f'    \033[0;31m Jogador, essa posição já tem uma jogada definida: {p[coluna][linha]}')
        coluna = int(input('\033[0;32mDigite uma coluna [1 a 3]: '))
        linha = int(input('\033[0;32mDigite uma linha [1 a 3]: '))
        resp = jogada(coluna, linha, 'X')

    mostratela()
    final += + 1
    validavencedor()

    if final < 6:
        coluna = int(randrange(1, 4))
        linha = int(randrange(1, 4))
        resp = jogada(coluna, linha, 'O')
        while not resp:
            coluna = int(randrange(1, 4))
            linha = int(randrange(1, 4))
            resp = jogada(coluna, linha, 'O')

        print('\033[0;37mComputador esta pensando...')
        sleep(0.5)
        # mostratela()

mostratela()
validavencedor()
print('\033[0;33mJOGO ACABOU, DEU VELHA!!!')
