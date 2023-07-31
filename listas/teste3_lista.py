n = int(input())
lista_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numeros_pares = ['0', '2', '4', '6', '8']
numeros_impares = ['1', '3', '5', '7', '9']
lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
palavra_final = ''
for i in range(n):
    palavra_decodificadora = input()
    if palavra_decodificadora == 'Portal':
        mensagem = input()
        palavra = ''
        for m in mensagem:
            if m in lista_letras:
                indice = int(lista_letras.index(i))
                proximo_indice = 1 + indice
                proxima_letra = lista_letras[proximo_indice]
                if palavra != '':
                    palavra = str(palavra) + str(proxima_letra)
                else:
                    palavra = str(proxima_letra)
        if palavra_final != '':
           palavra_final = palavra
        else:
            palavra_final = palavra_final, palavra
    elif palavra_decodificadora == 'Experiemento':
        mensagem = input()
        somatorio_pares = 0
        for m in mensagem:
            if m in numeros_pares:
                somatorio_pares += int(i)
        palavra = str(somatorio_pares)
        if palavra_final != '':
           palavra_final = palavra
        else:
            palavra_final = palavra_final, palavra

    elif palavra_decodificadora == 'Schembulock':
        mensagem = input()
        multiplicaçao = 1
        for m in mensagem:
            if m in lista_numeros:
                multiplicaçao = multiplicaçao * int(i)
        palavra = str(multiplicaçao)
        if palavra_final != '':
           palavra_final = palavra
        else:
            palavra_final = palavra_final, palavra

    elif palavra_decodificadora == 'Realidade':
        mensagem = input()
        somatorio_impares = 0
        for m in mensagem:
            if m in numeros_impares:
                somatorio_impares += int(i)
        palavra = str(somatorio_impares)
        if palavra_final != '':
           palavra_final = palavra
        else:
            palavra_final = palavra_final, palavra

print(palavra_final)