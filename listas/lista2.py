n = int(input())
cont2 = 0

diario1 = []
diario2 = []
diario3 = []

while cont2 < n:
    entrada = input()
    conteudo, numero_diario = entrada.split(', ')
    numero_diario = int(numero_diario)
    if numero_diario == 1:
        diario1.append(conteudo)
    elif numero_diario == 2:
        diario2.append(conteudo)
    elif numero_diario == 3:
        diario3.append(conteudo)
    cont2 +=1

m = int(input())
cont2 = 0

while cont2 < m:
    busca = input()
    if busca in diario1:
        print(f'Informacoes sobre {busca} estao no Diario 1')
    elif busca in diario2:
        print(f'Informacoes sobre {busca} estao no Diario 2')
    elif busca in diario3:
        print(f'Informacoes sobre {busca} estao no Diario 3')
    else:
      print(f'Nenhum dos diarios possui informacoes sobre {busca}')
    cont2 +=1