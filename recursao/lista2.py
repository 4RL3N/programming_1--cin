frase_invertida = []
frase_pronta = []

string = input() #Entrada
len_string = len(string)

def inserir_lista(lista_frase, tamanho_string): #Função que insere todos os termos da entrada 
    for i in range(tamanho_string):             #em uma lista
        lista_frase.append(string[i])
    return lista_frase

def f_pronta(frase_invertida, frase_pronta): #Ordena os itens da lista da forma correta
    if (len(frase_invertida)) <= 1:
        frase_pronta.append(frase_invertida[0])
    else:
        auxiliar = frase_invertida[-1]
        frase_pronta.append(auxiliar)
        del frase_invertida[-1]
        frase_pronta = f_pronta(frase_invertida, frase_pronta)

    return frase_pronta


frase_invertida = inserir_lista(frase_invertida, len_string) #Chama a Função que insere a entrada em uma lista

frase_final = f_pronta(frase_invertida, frase_pronta)

print(''.join(frase_final))