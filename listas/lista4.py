n = int(input())
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
frase = []
cond = True
mensagem = ''

for i in range(n):
    nada = input()
    palavra_decod = input()
    nada = input()
    entrada = input()
    soma = int()

    if i > 0:
        frase.append(' ')
    if palavra_decod == 'Portal':
        for letra in entrada:          
            if letra in alfabeto:
                indx_letra = int(alfabeto.index(letra))
                indx_final = indx_letra + 1
                if letra == 'z':
                    indx_final = 0
                frase.append(alfabeto[indx_final])
            else:
                continue
    elif palavra_decod == 'Experimento':
        for letra in entrada:
            if letra in numeros:
                letra = int(letra)
                resto = letra%2
                if resto == 0:
                    soma += letra
                else:
                    continue
        soma = str(soma)
        frase.append(soma)
    elif palavra_decod == 'Realidade':
        for letra in entrada:
            if letra in numeros:
                letra = int(letra)
                resto = letra%2
                if resto == 1:
                    soma += letra
                else:
                    continue
        soma = str(soma)
        frase.append(soma)
    elif palavra_decod == 'Schembulock':
        soma = 1
        for letra in entrada:
            if letra in numeros:
                letra = int(letra)
                soma*=letra
        soma = str(soma)
        frase.append(soma)
    else:
        continue

while ' ' in frase[-1]:
    frase.remove(frase[-1])

if len(frase) > 0:
    frase_completa = "".join(frase)
    print(f'Consegui! A mensagem decodificada de Bill Cipher é: {frase_completa}')

else:
    print('Esse formato de mensagem nem Bill Cipher entenderia!')