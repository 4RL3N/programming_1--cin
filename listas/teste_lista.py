#cria estoque
produtos_vendidos = ['alicate', 'faca', 'fio', 'cimento', 'ferro', 'tomada']
produtos_estoque = ['alicate', 'alicate', 'alicate', 'alicate', 'faca', 'faca', 'faca', 'fio', 'fio', 'fio', 'fio', 'fio', 'cimento', 'cimento', 'ferro', 'tomada', 'tomada', 'tomada', 'tomada' ]

vende = False
cond = True

# para não precisar reexecutar o código,
# criei um laço para fazer isso 
# automáticamente

while cond:
    entrada = input('Produto a ser consultado: ')
    if entrada == 'pare':
        print('Programa finalizado!')
        break

    #verifica se vende o produto
    for prod_vendido in produtos_vendidos:
        if  prod_vendido == entrada:
            vende = True

    if vende:
        #verifica a quantidade em estoque
        quantidade = 0
        for prod_estoque in produtos_estoque:
            if prod_estoque == entrada:
                quantidade +=1

    #output
    if not vende:
        print (f'Não vendemos')

    elif quantidade > 0:
        print(f'Temos {quantidade} {entrada}(s) em estoque')

    else:
        print(f'Não temos {entrada} disponível no momento em estoque')
