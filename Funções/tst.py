def soma_input(usuario, soma): #funcao para somar os inteiros dentro da lista
    numeros = list(range(10)) #cria uma lista com o nome numeros, de 0 a 9
    numeros = str(numeros) #transforma essa lista para str, para comparar com os itens da lista
    for i in usuario:
        if i == ' ': #adicionei esse if para ter certeza de nao dar bugs
            continue
        elif i in numeros:
            i = int(i)
            soma += i #caso seja um numero, some-os
    return soma

def transf_lista(nome, lista): #funcao simples para transofrmar uma entrada 'str' em lista
    for i in nome:
        lista.append(i)
    return lista

def compressao_usuario(lista_usuario, usu_comprimido): #funcao que comprime a mensagem do usuario
    num = 1
    if len(lista_usuario) == 1:
        num = 1
    
    elif lista_usuario[0] == lista_usuario[1]:
        while lista_usuario[0] == lista_usuario[1]: #caso os ultimos termos sejam iguais, conte-os
            num += 1
            lista_usuario.remove(lista_usuario[0])  #e vá removendo o ultimo termo   

            if len(lista_usuario) < 2: #caso a lista seja menor que 2, pare
                break    
        #else:
    usu_comprimido.append(str(num))     
    usu_comprimido.append(lista_usuario[0]) #insira na nova lista a letra correspondente e sua quantidade

    if len(lista_usuario) >= 2: #caso a lista seja maior que 1, refaca o processo
        resposta = compressao_usuario(lista_usuario[1:], usu_comprimido) #recursividade
        #usu_comprimido.append(resposta)

    return usu_comprimido

def descomp_chat(lista, mensagem_f): #funcao que descompacta a mensagem do chatgpt
    i = int(lista[0])
    for j in range(i):  
        mensagem_f.append(lista[1])  #adicione na nova lista a letra lista[i+1], (i) vezes
        
    if (len(lista) - 2) > 1:
        resposta = descomp_chat(lista[2::], mensagem_f) #recursividade
        #existe um padrao (a cada 1 itens é um int, comecando do primeiro)
        
    return mensagem_f

contador = 0
while True:
    entrada = input()
    if entrada == 'Preciso parar de usar o ChatGPT':
        break
    elif entrada == 'Vou pedir ajuda pro meu amigo ChatGPT':
        while True:
            usuario = input()
            if usuario == 'Não tô entendendo nada':
                break
            else:
                contador += 1
                
                lista = [] #define/redefine a lista como vazia
                lista_usuario = transf_lista(usuario, lista) #transforma a entrada em uma lista 
                
                usu_comprimido = []
                usuario_comprimido = compressao_usuario(lista_usuario, usu_comprimido) #funcao que comprime a entrada do usuario
                
                soma = 0
                soma_termos = soma_input(usuario_comprimido, soma) #soma os termos 
                
                if (soma_termos > 0) and (soma_termos <= 5):
                    chatgpt = '1t3a1 1f1a1c3i1n1h1o1 1n3e'
                elif (soma_termos > 6) and (soma_termos <= 20):
                    chatgpt = '1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o'
                elif (soma_termos > 21) and (soma_termos <= 30):
                    chatgpt = '1s6o1 1n1a1 1v1i1d2a1 1m4a1n1s3a'
                elif (soma_termos > 31) and (soma_termos <= 40):
                    chatgpt = '1v5a1 1e2s1t4u3d3a3r1 1r1a1p3a3z'
                elif soma_termos > 40:
                    chatgpt = '3e1s1t5u1d1a1 1n2a1o1 1p1r3a1 1t2u1 1v4e1r'
                
                lista_chat = []
                lista_chat = transf_lista(chatgpt, lista_chat) #transforma a mensagem do chatgpt em uma lista
                
                mensagem_f = []
                descomp_chatgpt = descomp_chat(lista_chat, mensagem_f) #descompacta a mensagem do chatgpt
                
                nome_concatenado = ''.join(usuario_comprimido)
                print(f'usuário:{nome_concatenado}')
                
                chat_concatenado = ''.join(lista_chat)
                print(f'ChatGPT:{chat_concatenado}')
                
    elif entrada == 'Qual era a tradução?':
        if contador > 0:
            frase = "".join(descomp_chatgpt)
            print(f'Descobri! É: {frase}, tá de brincadeira né?')
        else:
            print('Não tem nada pra traduzir')
                    