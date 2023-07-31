from random import randint
def jogo_adivinhacao():
    num = randint(0,100)
    acertou = False
    chute = int(input('Digite um número inteiro no intervalo [0-100]: '))
    while (not acertou):
        if (chute == num):
            print('Parabéns, você acertou o número!')
            acertou = True
        elif(chute > num):
            chute = int(input('Tente um número menor: '))
        else:
            chute = int(input('Tente um número maior: '))
    else:
        print('Fim de jogo!')
jogo_adivinhacao()
print('Tente acertar mais rápido! Vamos jogar novamente!')
jogo_adivinhacao()