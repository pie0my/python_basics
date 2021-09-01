from random import randint

import sys

resposta = randint(int(sys.argv[1]), int(sys.argv[2]))


while True:
    try:
        chute = int(input('escolhe um numero de 1 a 10:  '))
        if 0 < chute < 11:
            if chute == resposta:
                print('voce acertou')
                break
        else:
            print('de 1 a 10...')
    except ValueError:
        print('escolha um numero...')
        continue
