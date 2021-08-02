
import random


def adivinha_chute(chute, resposta):
    chute = int(input('escolha um numero de 1 a 15:  '))
    if 0 < chute < 16:
        if chute == resposta:
            print('voce acertou')
            return True
    else:
        print('de 1 a 15...')
        return False


if __name__ == "__main__":
    resposta = random.randint(1, 15)
    while True:
        try:
            chute = int(input('escolha um numero de 1 a 15:  '))
            if (adivinha_chute(chute, resposta)):
                break
        except ValueError:
            print('escolha um número')
            continue
