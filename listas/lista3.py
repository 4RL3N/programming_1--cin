n = int(input())
lista = [0, 1]
mensagem_decodificada = []
for i in range(n):
    
    coordenadas = input()
    z, x_y = coordenadas.split(" ")
    letra, y = x_y.split("-")
    letra = int(letra)
    y = int(y)
    z = int(z)
    
    for numero in range(z):
        termo = lista[-2] + lista[-1]
        lista.append(termo)
        
    item_lista = str(lista[z])
    indx_item1 = item_lista[letra]
    indx_item2 = item_lista[y]

    tabela_item = indx_item1+indx_item2
    tabela_item = int(tabela_item)
    mensagem_decodificada.append(chr(tabela_item))
    
for letra in mensagem_decodificada:
    print(letra, end = '')