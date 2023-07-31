n = int(input())

nota = 0
soma = 0
melhor_lugar = ''
pior_lugar = ''
maior_nota = 0
menor_nota = 0
empate = ''

for i in range (n):
    nome_lugar = str(input())
    
    while True:
        nota = int(input())
        empate = 0
        if nota < 0:
          break
        soma+=nota
    if i == 0:
        maior_nota = soma
        menor_nota = soma
        melhor_lugar = nome_lugar
        pior_lugar = nome_lugar
    else:
        if soma > maior_nota:
            maior_nota = soma
            melhor_lugar = nome_lugar
        
        elif soma < menor_nota:
            menor_nota=soma
            pior_lugar=nome_lugar
            
        elif soma == maior_nota:
            maior_nota = soma
            melhor_lugar = melhor_lugar+', '+ nome_lugar
            empate = True

    soma = 0
    
if empate == True:
  print(f'{melhor_lugar}\n'
  'Tantas opções')

else:
  print(f'{melhor_lugar} ganhou de lavada de {pior_lugar}, com {maior_nota} vs {menor_nota}')