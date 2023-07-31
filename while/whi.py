def decisao(n, lugares):
    melhor_lugar = None
    pior_lugar = None
    melhores = []
    piores = []
    maior_nota = 0
    pior_nota = 1000000
    for i in range(n):
        nome = lugares[i][0]
        notas = lugares[i][1:]
        total = sum(notas)
        if total > maior_nota:
            maior_nota = total
            melhor_lugar = nome
            melhores = [nome]
        elif total == maior_nota:
            melhores.append(nome)
        if total < pior_nota:
            pior_nota = total
            pior_lugar = nome
            piores = [nome]
        elif total == pior_nota:
            piores.append(nome)
    if len(melhores) > 1:
        return ', '.join(melhores)
    else:
        return f'{melhor_lugar} ganhou de lavada de {pior_lugar}, com {maior_nota} vs {pior_nota}'

n = int(input().strip())
lugares = []
for i in range(n):
    nome = input().strip()
    notas = []
    nota = int(input().strip())
    while nota >= 0:
        notas.append(nota)
        nota = int(input().strip())
    lugares.append([nome] + notas)
print(decisao(n, lugares))
