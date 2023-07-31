lista_final = []
nomeinimigo = input()
nomealiado = input()
clima = input()
mensagem = ''
contador_2 = -1
quantidade = 0
#termos = 0

while not mensagem  == 'Cansado':
    mensagem = input()
    if mensagem == 'Cansado':
        continue
    else:
        n1, n2, n3, n4, n5, n6, n7, n8, n9 = mensagem.split(" ")
        #termos +=9
        #m = 0
        #while m < termos:
            #nome_lista = f'lista_{m}'
        lista = []    
        lista.append(n1)
        lista.append(n2)
        lista.append(n3)
        lista.append(n4)
        lista.append(n5)
        lista.append(n6)
        lista.append(n7)
        lista.append(n8)
        lista.append(n9)

            #lista[nome_lista] = nova_lista

        #m += 1
        
        quantidade += 1

    if (clima == 'Ensolarado') or (clima == 'Nublado') or (clima == 'ChuvosoNormal') or (clima == 'ChuvosoComRaio'):   
        if clima == 'Ensolarado':
            n = len(lista)
            for contador in range(n):          #vai passar em cada item da lista
                for x in range(n - contador - 1):          #compara (n - i - 1) com cada elemento
                    if int(lista[x]) > int(lista[x + 1]):             #vai comparar cada item com o proximo
                        lista[x], lista[x + 1] = lista[x + 1], lista [x]            #vai trocar os items se não estiverem na ordem
            lista_final.append(lista)
        elif clima == 'Nublado':
            n = len(lista)
            for contador in range(n):
                for x in range(n - contador - 1):
                    if int(lista[x]) < int(lista[x + 1]):
                        lista[x + 1], lista[x] = lista[x], lista [x + 1]
            lista_final.append(lista)
        elif clima == 'ChuvosoNormal':
            n = len(lista)
            for x in range(n):
                #for x in range(n - contador):
                    try:
                        lista_l = lista_final[contador_2]
                        if int(lista[x]) < int(lista_l[x]):
                            lista_l[x], lista[x] = lista[x], lista_l[x]
                    except:
                        continue
            lista_final.append(lista)
            contador_2 += 1

        elif clima == 'ChuvosoComRaio':
            n = len(lista)
            for x in range(n):
                #for x in range(n - contador):
                    try:
                        lista_l = lista_final[contador_2]
                        if int(lista[x]) > int(lista_l[x]):
                            lista[x], lista_l[x] = lista_l[x], lista[x]
                    except:
                        continue
            lista_final.append(lista)
            contador_2 += 1

if (clima == 'Ensolarado') or (clima == 'Nublado') or (clima == 'ChuvosoNormal') or (clima == 'ChuvosoComRaio'):

    if (clima == 'Ensolarado'):
        print(f'Caramba! Finalmente organizamos a mensagem secreta do {nomeinimigo} com esse clima Ensolarado! Vamos nessa {nomealiado}!')

    elif (clima == 'Nublado'):
        print(f'Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do {nomeinimigo}! Vamos nessa {nomealiado}!')                   

    elif (clima == 'ChuvosoNormal'):
        print(f'Nem mesmo a chuva vai nos parar de salvar o mundo! Desvendamos a mensagem do {nomeinimigo}! Vamos nessa {nomealiado}!')
                
    elif (clima == 'ChuvosoComRaio'):
        print(f'Eitaa! Até mesmo essa chuva com trovoadas não nos parou. Estamos indo até você, {nomeinimigo}! Vamos nessa {nomealiado}!')
        
    print(f'Agora decodificamos as {quantidade} mensagens do {nomeinimigo} e sabemos seus {quantidade} lugares de ataque.')
    print('Os lugares sao:')
    posicao = 0
    lugar = 1
    indice = len(lista_final)
    for i in range(indice):

        termo = lista_final[posicao]
        print(f'{lugar} lugar:')
        print(f"Coordenadas: {termo[0]}° {termo[1]}' {termo[2]}''")
        print(f'Horario: {termo[3]}h {termo[4]}m {termo[5]}s')
        print(f'Data: {termo[6]}/{termo[7]}/{termo[8]}')
                    
        posicao += 1
        lugar += 1

    print(f'Vamos rapido {nomealiado}!!')

else:
    print('Infelizmente esse clima não está bom. Não conseguimos decifrar a mensagem, o que será do mundo agora??')
    print(f'Tenho certeza que conseguiremos na próxima {nomealiado}')