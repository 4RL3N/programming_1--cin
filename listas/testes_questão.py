lista = []
nomeinimigo = input()
nomealiado = input()
clima = input()
mensagem = ''
quantidade = 0

while not mensagem  == 'Cansado':
    mensagem = input()
    if mensagem == 'Cansado':
        continue
    else:
        n1, n2, n3, n4, n5, n6, n7, n8, n9 = mensagem.split(" ")
        lista.append(n1)
        lista.append(n2)
        lista.append(n3)
        lista.append(n4)
        lista.append(n5)
        lista.append(n6)
        lista.append(n7)
        lista.append(n8)
        lista.append(n9)
        quantidade += 1

    if (clima == 'Ensolarado') or (clima == 'Nublado') or (clima == 'ChuvosoNormal') or (clima == 'ChuvosoComRaio'):   
        if clima == 'Ensolarado':
            n = len(lista)
            for i in range(n):          #vai passar em cada item da lista
                for x in range(n - i - 1):          #compara (n - i - 1) com cada elemento
                    if lista[x] > lista[x + 1]:             #vai comparar cada item com o proximo
                        lista[x], lista[x + 1] = lista[x + 1], lista [x]            #vai trocar os items se não estiverem na ordem
            print(f'Caramba! Finalmente organizamos a mensagem secreta do {nomeinimigo} com esse clima Ensolarado! Vamos nessa {nomealiado}!')
        elif clima == 'Nublado':
            n = len(lista)
            for i in range(n):
                for x in range(n - i - 1):
                    if lista[x] < lista[x + 1]:
                        lista[x + 1], lista[x] = lista[x], lista [x + 1]
            print(f'Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do {nomeinimigo}! Vamos nessa {nomealiado}!')
        elif clima == 'ChuvosoNormal':
            n = len(lista)
            for i in range(n):
                for x in range(n - i):
                    try:
                        lista[x] = int(lista[x])
                        if (lista[x]) < (lista[x + 9]):
                            lista[x], lista [x + 9] = lista[x + 9], lista[x]
                    except:
                        continue
            print(f'Nem mesmo a chuva vai nos parar de salvar o mundo! Desvendamos a mensagem do {nomeinimigo}! Vamos nessa {nomealiado}!')
        elif clima == 'ChuvosoComRaio':
            n = len(lista)
            for i in range(n):
                for x in range(n - i):
                    try:
                        lista[x] = int(lista[x])
                        if (lista[x]) > (lista[x + 9]):
                            lista[x + 9], lista [x] = lista[x], lista[x + 9]
                    except:
                        continue
            print(f'Eitaa! Até mesmo essa chuva com trovoadas não nos parou. Estamos indo até você, {nomeinimigo}! Vamos nessa {nomealiado}!')
    
    print(f'Agora decodificamos as {quantidade} mensagens do {nomeinimigo} e sabemos seus {quantidade} lugares de ataque.')
    print('Os lugares sao:')
    posicao = 1

    quantidade = str(quantidade)
    for lugares in quantidade:
        print(f'{posicao} lugar:')
        print(f"Coordenadas: {lista[0]}° {lista[1]}' {lista[2]}''")
        print(f'Horario: {lista[3]}h {lista[4]}m {lista[5]}s')
        print(f'Data: {lista[6]}/{lista[7]}/{lista[8]}')
        posicao += 1

    print(f'Vamos rapido {nomealiado}!')

else:
    print('Infelizmente esse clima não está bom. Não conseguimos decifrar a mensagem, o que será do mundo agora??')
    print(f'Tenho certeza que conseguiremos na próxima {nomealiado}')