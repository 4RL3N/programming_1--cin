frase1 = str(input())

contador = 0

f1 = (frase1 == 'O relógio descarregou!')
f2 = (frase1 == 'Por hoje já deu')

while not f1 and not f2:
    contador+=1
    frase1 = input()
    f1 = (frase1 == 'O relógio descarregou!')
    f2 = (frase1 == 'Por hoje já deu')
    
else:
    if frase1 == 'O relógio descarregou!':
        print(f'Corra Ben! Você já derrotou {contador} aliens')
    elif frase1 == 'Por hoje já deu':
        print(f'Muito Ben Ben! hehe você derrotou {contador} aliens hoje')