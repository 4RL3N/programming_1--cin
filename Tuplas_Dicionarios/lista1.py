def aniver(m, todos_animais):
  try:
    animal = todos_animais.pop()
    valor = animal['mes']
    if valor == m:
        nome1 = animal.pop('nome')
        especie1 = animal.pop('especie')
        aniversariantes_do_mes.append(nome1)
        aniversariantes_do_mes.append(especie1)
  
    aniver(m, todos_animais)
  
  except:
    return

n = int(input())
dados_animais = []
todos_do_mes = []
aniversariantes_do_mes = []
cont = 0
for i in range(n):
  nome, especie, data_nascimento = input().split(' ')
  dia, mes, ano = data_nascimento.split('/')
  
  dicionario  = {}
  dicionario['nome'] = nome
  dicionario['especie'] = especie
  dicionario['mes'] = mes
  
  dados_animais.append(dicionario)

m = str(input())

if len(m) == 1:
  m = '0'+ m

aniver(m, dados_animais) #quais animais fazem aniversario no mes 'm'


for i in range(int(len(aniversariantes_do_mes)/2)):
  dicionario  = {}
  nome1 = aniversariantes_do_mes.pop(0)
  especie1 = aniversariantes_do_mes.pop(0)
  dicionario['nome'] = nome1
  dicionario['especie'] = especie1

  todos_do_mes.append(dicionario)

#dicionario_ordenado = dict(sorted(todos_do_mes.items()))


dicionario_ordenado = sorted(todos_do_mes, key=lambda x: x["nome"])

if len(dicionario_ordenado) > 0: 
  print('E os donos da festa do mes sao:')
  for dicionario in dicionario_ordenado:
    print(f'{dicionario[nome]} - {dicionario[especie]}')

else:
  print('Sem festa esse mes. :(')