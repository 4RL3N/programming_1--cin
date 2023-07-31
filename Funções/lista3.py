vilao = ['Makima', 'Reze', 'Santa Claus'] #Lista com os nomes dos viloes
resultado = [] #Resultados das lutas
motosserra = [] #Transformacoes das motosserras
v = 0 #Numero de Vitorias
d = 0 #Numero de Derrotas
e = 0 #Numero de Empates

rodada = 1 #Numero da Rodada
indice_vilao = 0 #Indice do vilao na lista de viloes

def prints(): #Criei uma funcao com os prints para simplificar no final
    if v == 3: #Se Denji ganhar as 3 batalhas:
        print('Nenhum dos 3 inimigos foram capazes de derrotar o Denji!')

    elif d == 3: #Se Denji perder as 3 batalhas
        print('Hoje não foi um dia bom para o Denji, perdeu todas as batalhas')

    elif (v== 1) and (d == 1) and (e == 1): #Caso Denji perca, ganhe e empate uma 
        print('Hoje foi um dia equilibrado para o Denji, conseguiu ganhar, perder e empatar')

    elif (v == 2): #Caso Denji ganhe duas batalhas
        print('Denji conseguiu derrotar a maioria de seus inimigos')

    elif d == 2: #Caso Denji perca duas batalhas
        print('Dia péssimo para o Denji, perdeu a maioria de suas batalhas')

    elif e == 2: #Caso Denji empate duas batalhas
        print('Dia duro para o Denji, empatou de mais')

def tipo_motosserra():
    if (energia >= 750) and (controle >= 7) and (precisao >= 8):
        return 'Motosserra Suprema'

    elif (energia >= 500) and (controle >= 6) and (precisao >= 6):
        return 'Motosserra Avançada'

    else:
        return 'Motosserra Normal'

while rodada <= len(vilao):

    energia = int(input())
    controle = int(input())
    precisao = int(input())
    forca_inimi = int(input())
    forca_denji = energia+(controle*precisao)

    classificacao = tipo_motosserra() #Tipo da motosserra
        
    motosserra.append(classificacao) #Insira o tipo de motosserra na lista

    print(f'### Rodada {rodada} - {vilao[indice_vilao]} ###')

    print(f'O Denji ira se transformar na {classificacao} para enfrentar o {vilao[indice_vilao]}')

    if forca_denji > forca_inimi:
        print(f'Denji saiu vitorioso nessa batalha contra o {vilao[indice_vilao]}')
        resultado.append('Vitoria')
        v += 1

    elif forca_inimi > forca_denji:
        print(f'Denji não conseguiu força o suficiente para derrotar o {vilao[indice_vilao]}')
        resultado.append('Derrota')
        d += 1

    else:
        print(f'Como pode ser possível?? Denji possui a mesma força que o {vilao[indice_vilao]}')
        resultado.append('Empate')
        e += 1


    rodada+=1
    indice_vilao+=1

print(f'### Resultado Final ###')

rodada = 1

for i in range(len(resultado)):
    print(f'Rodada {rodada}: {motosserra[i]} - {resultado[i]}')
    rodada += 1

prints()