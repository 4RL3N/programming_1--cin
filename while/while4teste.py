cond = True
cond2 = True
etapa = 0
custo_total = 0
etapas_realizadas = 0
total_falhas = 0

nome_invencao = str(input())

while cond:
    nome_etapa = str(input())
    if (nome_etapa == 'concluir') or (nome_etapa == 'desistir'):
        print(f'A jornada da construção do(a) {nome_invencao} acaba aqui.')
        cond = False
    elif nome_etapa == 'dar um plus':
        custo_etapa = int(input())
        custo_total += custo_etapa
        print(f'Agora o(a) {nome_invencao} ficou ainda mais legal! Pena que precisei gastar R${custo_etapa}')
    else:
        custo_etapa = int(input())
        tentativas_etapa = int(input())
        for i in range(tentativas_etapa):
            if cond2:
                status_etapa = str(input())
                if status_etapa == 'correto':
                    etapa += 1
                    custo_total += custo_etapa
                    print(f'Oba! consegui {nome_etapa}, o que me custou R${custo_etapa}')
                    print(f'ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {total_falhas}')
                    cond2 = False
                else:
                    total_falhas += 1
                    custo_total+=custo_etapa
                    print(f'Ainda não consegui {nome_etapa} corretamente, e essa tentativa me custou R${custo_etapa}')
                if i == (tentativas_etapa - 1) and (status_etapa != 'correto'):
                    print(f'ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {total_falhas}')
                    condicao = False
    
if nome_etapa == 'desistir':
    print (f'Infelizmente, o sonho do(a) {nome_invencao} foi interrompido e levou junto com ele R${custo_total}')
else:
    print(f'Uhuuu, finalmente o(a) {nome_invencao} tá pronto(a)! Esse projeto me custou R${custo_total}')
