n = int(input())

lista_primos = []
primo = ''
c1 = n%2
c2 = n%3
c3 = n%5
c4 = n%7
m = n

def descobrir_primo():
    #Descobrir se é primo
    #Ele vai checar caso o resto da divisão for zero, o numero não é primo
    global cond #Precisa ser uma variavel golbal para funcionar fora do "def"

    c1 = n%2 #Essa area descobre se o "n" é multiplo desses numeros
    c2 = n%3
    c3 = n%5
    c4 = n%7

    if (n == 1) or (n == 0): #1 não é divisível por 2 numeros, apenas por ele mesmo
        cond = False #0 não é divisível
    elif (c1 == 0) or (c2 == 0) or (c3 == 0) or (c4 == 0):
        cond = False
        if n == 2:     #Caso "n" for o proprio numero, a condição recebe verdadeiro
            cond = True
        if n == 3:
            cond = True
        if n == 5:
            cond = True
        if n == 7:
            cond = True
    else:
        cond = True

descobrir_primo() #Descobre se "n" é primo, acionando a função

if cond:
    print(f'O número {m} é primo.') #Caso o "n" for primo
else:
    print(f'O número {m} não é primo.') #Caso "n" não for primo...

    for i in range(m): #Descobrir quais os numeros primos de 1 a "n"
        n = i #"n" vai receber o valor de "i", para poder verificar se "i" e primo
        descobrir_primo()
        if cond:
            lista_primos.append(str(i)) #Caso "n" for primo, guarde em uma lista
            lista_primos.append(', ')
        
    if len(lista_primos) >= 1: #Caso a lista de primos tiver algum item
        print(f'Entretanto, temos primos no intervalo de 1 à {m}. Estes são:')

        lista_primos.pop(-1) #Remove o ultimo termo da lista, pois é um ", "
        
        for x in range(len(lista_primos)): #Concatena os itens da lista,e os guarda em "Primo"
            primo += lista_primos[x]

        print(primo)
    
    else: #Caso não tiver numero primo no intervalo
        print(f'Além disso, não temos primos no intervalo de 1 à {m}.')

print('AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!')