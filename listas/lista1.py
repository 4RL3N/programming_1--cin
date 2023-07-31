cond = True
lista = []
contador = 0

while cond:
    entrada = input()
    if entrada == 'novo suspeito - altissima periculosidade':
        nome = input()
        lista.insert(0, nome)

    elif entrada == 'novo suspeito - pouco perigoso':
        nome = input()
        lista.append(nome)

    elif entrada == 'livre de suspeita, pode remover':
        nome = input()
        lista.remove(nome)

    elif entrada == 'sujeito mais perigoso do que pensavamos':
        indx = int(input())
        indx_atualizado = int(input())
        item = lista.pop(indx)
        lista.insert(indx_atualizado, item)

    elif entrada == 'que estranho, esses dois meliantes… troque-os de lugar':
        nome1 = input()
        idx1 = lista.index(nome1)
        lista.remove(nome1)
        nome2 = input()
        idx2 = lista.index(nome2)
        lista.remove(nome2)
        lista.insert(idx2, nome1)
        lista.insert(idx1, nome2)

    elif entrada == 'essa posicao nao esta de acordo, ele nao e tao perigoso assim':    
        nome = input()
        lista.remove(nome)
        lista.append(nome)
    
    elif entrada == 'como a lista esta ficando?':
        print(lista, sep=' ', end='')

    elif entrada == 'ja temos nossa lista de suspeitos':
        print('O resultado final ficou assim:')
        print(lista, sep=' ', end='')
        break