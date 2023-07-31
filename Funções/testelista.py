celas = []

def contador_ascii(): #Essa função irá processar o nome do demonio, e retornar o seu indice na cela
    valor = []
    for x in range(len(nome_demo)):
          valor_ascii = ord(nome_demo[x])
          valor.append(valor_ascii)
    valor_ascii = 0
    for y in range(len(valor)):
        valor_ascii += valor[y]

    indice_cela = valor_ascii % int(quantidade_celas)

    return indice_cela

def nome_presos(): 
  presos = ''
  for item in range(len(celas)):
      if celas[item] != '':
          presos += celas[item] + ' '
          
  if presos[-1] == ' ':
      presos = presos[:-1]
      
  return presos

entrada = input()

quantidade_celas, quantidade_ordens = entrada.split(' ')

for i in range(int(quantidade_celas)): #Criar a quantidade de celas
    celas.append('')

for i in range(int(quantidade_ordens)): #Executar as ordens

    entrada_2 = input()
    ordem, nome_demo = entrada_2.split(' ')

    if ordem == 'REMOVER':
        if nome_demo in celas:
            indx = celas.index(nome_demo)
            celas[indx] = ''
        
        elif nome_demo not in celas:
            print('NAO EXISTE')
            
    else: 
      indice_cela = contador_ascii()
        
      if celas[indice_cela] == '':
          celas[indice_cela] = nome_demo
          
      else:
          for z in range(indice_cela, len(celas)):
              if celas[z] == '':
                  celas[z] = nome_demo
                  break
                 
          if nome_demo not in celas:
              for a in range(0, indice_cela):
                  if celas[a] == '':
                      celas[a] = nome_demo
                      break
                     
          if nome_demo not in celas:
              print('Cheio')

presos = nome_presos()

print(presos)