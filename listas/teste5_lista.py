lista_alunos = ['rui', 'heloisa', 'augusto', 'heloisa', 'leticia']
lista2 = ['arlenzinho', 'david']
cond = True

while cond:
    entrada = input('Digite: ')
    if entrada == 'pare':
        break
    if entrada == 'remover':
        lista_alunos.remove('heloisa')
    elif 'remover ' in entrada:
        aluno = lista_alunos.pop(-1)
    else:
        lista_alunos.insert(0, entrada)
    print(lista_alunos)
    lista1 = lista_alunos + lista2
    print(lista1)

'''
print(f'index: {lista_alunos.index("heloisa", 2)}')
lista_alunos.sort()
print(lista_alunos)
lista_alunos.sort(reverse=True)
print(lista_alunos)
lista_alunosAtoZ = sorted(lista_alunos)
print(f'Lista normal: {lista_alunos}')
print(f'Lista A para Z: {lista_alunosAtoZ}')
entrada = input('digite: ')
lista_alunos.insert(2, entrada)
print(lista_alunos)
'''