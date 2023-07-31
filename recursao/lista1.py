def seq(i, razao):
    if i == 0:
        w = n1
        return w
    elif i == 1:
        w = n2
        return w
    elif i == 2:
        w = n3
        return w
    else:
        item = razao + seq(i - 1, razao)
        return item

def raz(x, y, z):
    a = z - y
    b = y - x
    if a == b:
        return a


sequencia = []

prim_prog = input()
busca = int(input())

n1, n2, n3 = prim_prog.split(' ')

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

razao = raz(n1, n2, n3)

for i in range(busca + 1):
    sequencia.append(seq(i, razao))

print(f'Na progressão aritmética cujos três primeiros números são {n1}, {n2} e {n3}, o {busca}º elemento é {sequencia[busca - 1]} e a razão da progressão é {razao}.')