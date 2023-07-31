lista = ['1', '2', '7', '9', '34', '51']

qnt = len(lista)
metade = int(qnt/2)

lista1 = (lista[0:metade])
lista2 = (lista[metade:])
'''
soma1 = int(lista1[0]) + int(lista2[0])
soma2 = int(lista1[1]) + int(lista2[1])
soma3 = int(lista1[2]) + int(lista2[2])
lista_soma = [f'{soma1}', f'{soma2}', f'{soma3}']
'''
lista_soma = []
for indice in range(metade):
    lista_soma.append(int(lista1[indice]) + int(lista2[indice]))

print(lista1)
print(lista2)
print(lista_soma)

