todos_animais = {

    'gato' : {
        'nessec' : ['bola de lã', 'caixa de areia', 'ração', 'ratinho de brinquedo' ],
        #'inimigos' : ['cachorro', 'hamster', 'peixe']
        'inimigos' : ['peixe', 'hamster', 'cachorro']
        },
                      
    'cachorro' : {
        'nessec' : ['coleira', 'ração', 'ursinho de pelúcia'],
        'inimigos': ['gato']
        },

    'peixe' : {
        'nessec':['aquário',  'filtro', 'ração'],
        'inimigos' : ['gato']
        },

    'hamster' : {
        'nessec' : [ 'ração', 'roda para hamster', 'serragem'],
        'inimigos' : ['cachorro', 'gato']
        }
}

filhote = False
cond = True

###

entrada = input()

if ' e ' in entrada:
    animais = entrada.split(' e ')

else:
    animais = entrada

###

n = input()

if n == 'sim':
    filhote = True

for i in animais:
    if i not in todos_animais:
        print(f'Sérgio, o animal {i} não estava nas suas potenciais escolhas, logo ele não pode ser analisado.')
        cond = False

if cond:
    if filhote:
        print('Como os animais são recém nascidos, eles podem ser adotados juntos!')
        print('Segue aqui as necessidades dos animais:')
        for i in animais:
            print(f'As necessidades do(a) {i} são:')
            for j in range(len(todos_animais[i]['nessec'])):
                print(f'- {todos_animais[i]["nessec"][j]};')

        print('Dito isso, vamos adotá-los!!!')
    
    else:
        for i in animais:
            condicao = True
            for j in todos_animais[i]['inimigos']:
                if j in animais:
                    print(f'Sérgio, o(a) {i} tem o(a) {j} como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos')
                    condicao = False
         
        if condicao:
          print(f'Segue aqui as necessidades dos animais:')
          for i in animais:
                print(f'As necessidades do(a) {i} são:')
                for k in range(len(todos_animais[i]['nessec'])):
                    print(f'- {todos_animais[i]["nessec"][k]};')  
          print('Dito isso, vamos adotá-los!!!')

