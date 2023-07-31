#cria estoque
produtos_vendidos = ['alicate', 'faca', 'fio', 'cimento', 'ferro', 'tomada', 'tesoura']
produtos_estoque = ['alicate', 'alicate', 'alicate', 'alicate', 'faca', 'faca', 'faca', 'fio', 'fio', 'fio', 'fio', 'fio', 'cimento', 'cimento', 'ferro', 'tomada', 'tomada', 'tomada', 'tomada' ]

vende = False

for produtos in produtos_vendidos:
    #consulta produtos em estoque
    quantidade = 0
    for prod_estoque in produtos_estoque:
        if prod_estoque == produtos:
            quantidade += 1
    print(f'Existem {quantidade} {produtos} em estoque!')