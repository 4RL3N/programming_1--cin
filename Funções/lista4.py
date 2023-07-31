celas = []

def contador_ascii(letras_demo, nome_demo): #Essa função irá processar o nome do demonio, e retornar o seu indice na cela
    valor = []
    for x in range(letras_demo): #O primeiro for descobre os valores unicode de cada letra do nome do demo
          valor_ascii = ord(nome_demo[x])
          valor.append(valor_ascii) #e guarda o valor em uma lista
    valor_ascii = 0
    for y in range(len(valor)): #o segundo for soma os valores unicode de cada letra do nome demo, armazenado na lista
        valor_ascii += valor[y]

    indice_cela = valor_ascii % int(quantidade_celas)

    return indice_cela #retorna o indice da cela

def nome_presos(n_celas): #Função que concatena os valores da lista dos nomes dos demos
  presos = ''
  for item in range(n_celas):
      if celas[item] != '': #se a cela estiver ocupada, concatene os valores para o print final
          presos += celas[item] + ' '
          
  if presos[-1] == ' ': #no final, caso o ultimo caractere seja um espaço em branco, remova-o
      presos = presos[:-1]
      
  return presos #retorne os nomes dos presos

entrada = input()

quantidade_celas, quantidade_ordens = entrada.split(' ')

for i in range(int(quantidade_celas)): #Criar a quantidade de celas
    celas.append('')

for i in range(int(quantidade_ordens)): #Executar as ordens

    entrada_2 = input() #vai receber a ordem e o nome do demonio
    ordem, nome_demo = entrada_2.split(' ')
    
    len_demo = len(nome_demo)
    indice_cela = contador_ascii(len_demo, nome_demo) #chama e atribui o valor da funcao a variavel indice_cela, passando parametros para a funcao
    
    if ordem == 'REMOVER':
        if nome_demo in celas:
            indx = celas.index(nome_demo) #o nome do demo pode ter sido alocado em outra cela por o indice original ja estar ocupado
            celas[indx] = '' #assim, temos que procurar o nome na lista, achar seu novo indice e remover
        else:
            print('NAO EXISTE')
          
    else: 
      if celas[indice_cela] == '':
          celas[indice_cela] = nome_demo #caso a cela esteja vazia, pode colocar o demo
          
      else:
          for z in range(indice_cela, len(celas)): #caso contrario, esse for irá procurar uma cela vazia á direita começando a busca a partir do indice do nome demo
              if celas[z] == '':
                  celas[z] = nome_demo
                  break
                 
          if nome_demo not in celas: #caso não encontre cela vazia a direita do indice a busca recomeca, dessa vez a partir do inicio das celas até o indice final
              for a in range(0, indice_cela):
                  if celas[a] == '':
                      celas[a] = nome_demo
                      break
                     
          if nome_demo not in celas: #caso ainda não encontre cela vazia, todas as celas estão ocupadas
              print('CHEIO')

qnt_celas = len(celas)
presos = nome_presos(qnt_celas)

print(presos)