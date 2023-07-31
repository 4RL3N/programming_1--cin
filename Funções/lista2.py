nome = ''
nome_sim = []
nome_nao = []
probab_sim = []
probab_nao = []

def organize(): #Função de organizar os dados
    probab = int(input())

    if (probab <= 50) or (nome == 'Makima'): #Caso a probabilidade for menor que 50, ou o nome for "Makima"
        print(f'Beleza {nome}!! Essa deve ser molezinha!')
        nome_sim.append(nome) #Adicione o nome na lista em que Denji tem possibilidade de sobreviver
        probab_sim.append(probab) #Adicione também a probabilidade da garota querer matá-lo

    else:
        print(f'{nome}, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?')
        nome_nao.append(nome) #Caso contrário, adicione o nome a lista de garotas que Denji deve evitar
        probab_nao.append(probab) #Adicione também a recpectiva possibilidade da garota querer matar Denji

while nome != 'cabo':
    nome = input()

    if nome == 'cabo': #Caso o o usuáio digite "cabo" encerre o while
        break

    prim_duas_letras = nome[0]+nome[1] 

    if len(nome) > 7: #Caso o nome tenha mais de 7 caracteres, recomece o while
        print(f'Er {prim_duas_letras}.. errr... nao consigo lembrar, melhor deixar para la')
        continue

    if nome == 'Makima':
        print('Woof Woof')

    organize() #Chame a função para organizar os dados

if len(nome_sim) > len(nome_nao): #Caso tenha mais pretendentes que garotas querendo matar Denji, printe:
    print('Epa ai sim! E hoje pochita!!')

else:
    print('Desculpa pochita acho que nao vai ser hoje que voce vai poder ver meus sonhos')

if len(nome_nao) == 0: #Caso não tenha nenhuma garota querendo matar Denji entre as pretendentes, a condição recebe verdadeiro
    cond = True
else:
    cond = False

if cond:
    for x in range(len(probab_sim)): #Para cada item da lista de pretendentes
        print(f'nome: {nome_sim[x]} - chances de morrer: {probab_sim[x]}%') #Imprima o nome da garotaa, e sua probabilidade