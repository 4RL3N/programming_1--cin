lista_de_animais = ['gato', 'cachorro', 'peixe', 'hamster']
necessidades_gato = ('bola de lã', 'caixa de areia', 'ração', 'ratinho de brinquedo')
necessidades_cachorro = ('coleira', 'ração', 'ursinho de pelúcia')
necessidades_peixe = ('aquário', 'filtro', 'ração')
necessidades_hamster = ('serragem', 'ração', 'roda para hamster')
gato_inimigos = ('cachorro', 'peixe', 'hamster')
cachorro_inimigos = ('gato')
peixe_inimigos = ('gato')
hamster_inimigos = ('gato', 'cachorro')


animais_dentro = []
animal_fora = []
gato = {'nome': 'gato', 'necessidades': necessidades_gato, 'inimigo': gato_inimigos}
cachorro = {'nome': 'cachorro', 'necessidades' : necessidades_cachorro, 'inimigo' : cachorro_inimigos}
peixe = {'nome': 'peixe', 'necessidades' : necessidades_peixe, 'inimigo':peixe_inimigos}
hamster = {'nome': 'hamster', 'necessidades' : necessidades_hamster, 'inimigos': hamster_inimigos}

entrada_animais = input().split(' e ')
recem_n_s_ou_n = input()

for animal in entrada_animais:
    if not(animal in lista_de_animais):
        animal_fora.append(animal)
    else:
        animais_dentro.append(animal)

if animal_fora != []:
    for i in animal_fora:
       print(f'Sérgio, o animal {animal_fora} não estava nas suas potenciais escolhas, logo ele não pode ser analisado.')

else:
    if recem_n_s_ou_n == 'sim':
        print('Como os animais são recém nascidos, eles podem ser adotados juntos!')
        print('Segue aqui as necessidades dos animais:')
        for i in animais_dentro:
            print(f'As necessidades do(a) {i} são:')
            for j in [i]['necessidades']:
                print(f'-{j};')


        print('Dito isso, vamos adotá-los!!!')