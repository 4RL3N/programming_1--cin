nome_invencao = str(input())

despesa_total = 0
cond = True

nome_etapa=str(input())
custo_etapa = int(input())
tentativas_etapa = int(input())

for i  in range(tentativas_etapa):
    nome_etapa=str(input())

    pare = (nome_etapa == 'desistir') or (nome_etapa == 'concluir')
    plus = (nome_etapa == 'dar um plus')

    if pare:
        print(f'A jornada da construção do(a) {nome_invencao} acaba aqui.')
        break
    elif plus:
        print (f'Agora o(a) {nome_invencao} ficou ainda mais legal! Pena que precisei gastar R${custo_etapa}')
    
    custo_etapa = int(input())
    despesa_total += custo_etapa
    tentativas_etapa = int(input())
        
    status_etapa = str(input())


