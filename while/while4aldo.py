nome_invencao = input()
etapas_realizadas = 0
falhas = 0
despesa_total = 0
condicao = True
going = True

while going:
    condicao = True
    nome_etapa = input()
    if nome_etapa == "desistir" or nome_etapa == "concluir":
        print(f'A jornada da construção do(a) {nome_invencao} acaba aqui.')
        going = False
    elif nome_etapa == "dar um plus":
        custo = int(input())
        despesa_total += custo
        print(f'Agora o(a) {nome_invencao} ficou ainda mais legal! Pena que precisei gastar R${custo}')
    else:
        custo = int(input())
        tentativas_etapa = int(input())
        for i in range(tentativas_etapa):
            if condicao:
                status_etapa = input()
                if status_etapa == "correto":
                    etapas_realizadas += 1
                    despesa_total += custo
                    print(f'Oba! consegui {nome_etapa}, o que me custou R${custo}')
                    print(f'ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {falhas}')
                    condicao = False
                else:
                    falhas += 1
                    despesa_total += custo
                    print(f'Ainda não consegui {nome_etapa} corretamente, e essa tentativa me custou R${custo}')
                if i == (tentativas_etapa - 1) and status_etapa != "correto":
                    print(f'ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {falhas}')
                    condicao = False

if nome_etapa == "desistir":
    print(f'Infelizmente, o sonho do(a) {nome_invencao} foi interrompido e levou junto com ele R${despesa_total}')
else:
    print(f'Uhuuu, finalmente o(a) {nome_invencao} tá pronto(a)! Esse projeto me custou R${despesa_total}')