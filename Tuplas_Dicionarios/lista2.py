def resultados(lista):
  for i in lista:
      i['media'] = float(i['media'])

  for i in lista:
      if i['media'] > 3:
          aprovacao.append(i)
      elif i['media'] < 2:
          reprov_direta.append(i)
      else:
          recuperacao.append(i)

m = int(input())
dados = []
aprovacao = []
reprov_direta = []
recuperacao = []

for i in range(m):
    nome, raca, ativ, obed, soci = input().split(', ')
    dicionario = {}
    dicionario['nome'] = nome
    dicionario['raca'] = raca
    dicionario['ativ'] = float(ativ)
    dicionario['obed'] = float(obed)
    dicionario['soci'] = float(soci)

    media = float(ativ)+float(obed)+float(soci)
    media = media/3
    media = (f'{media:.2f}')
    dicionario['media'] = media

    dados.append(dicionario)

resultados(dados)

if len(aprovacao) > 0:
    print('Estao aprovados e de parabens os seguintes coleguinhas:')
    for i in aprovacao:
        #i["media"] = "{:.1f}0".format(media)
        print(f'{i["nome"]} - {i["raca"]} - média: {i["media"]}')

if len(reprov_direta) > 0:
    print('Os colegas a seguir nao se comportaram bem e precisam de ajuda profissional (entrar em contato urgente):')
    for i in reprov_direta:
        print(f'{i["nome"]} - {i["raca"]} - média: {i["media"]}')

if len(recuperacao) > 0:
    print('Esses queridos terao uma nova chance e prometem melhorar:')
    for i in recuperacao:
        print(f'{i["nome"]} - {i["raca"]} - média: {i["media"]}')