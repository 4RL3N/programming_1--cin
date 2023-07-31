texto_1 = 'Férias inesquecíveis estão te esperando!'

texto_11 = 'Seu destino será Porto de Galinhas (BRA).'
texto_12 = 'Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!'

texto_21 = 'Seu destino será Fernando de Noronha (BRA).'
texto_22 = 'Belíssimas praias estão por vir.'
texto_23 = 'Não esqueça o protetor solar.'

texto_31 = 'Seu destino será Gramado (BRA).'
texto_32 = 'Aproveite passeios e paisagens espetaculares no sul do país!'

texto_41 = 'Seu destino será Berlim (ALE).'
texto_42 = 'Desfrute de muita cultura e de experiências incríveis!'
texto_43 = 'Prepare os casacos de frio!'

texto_51 = 'Seu destino será Tóquio (JPN).'
texto_52 = 'Viva uma experiência inesquecível explorando um país do outro lado do mundo.'
texto_53 = 'Prepare-se para muitas horas de voo!'





n_binario = input()

cond = True
tentativas = 3

decimal = 0
expoente = len(n_binario)-1

for i in n_binario:
    decimal += int(i) * (2**expoente)
    expoente -= 1

while cond:
    tentativas -=1
    palpite = float(input())

    if (palpite == decimal) and (tentativas >=0):
        print('Parabéns!! Você acertou!')
        if palpite == 1:
            print (texto_1)
            print(texto_11)
            print(texto_12)
            cond = False
            break
        elif palpite == 2:
            print(texto_1)
            print(texto_21)
            print(texto_22)
            print(texto_23)
            cond = False
            break
        elif palpite == 3:
            print(texto_1)
            print(texto_31)
            print(texto_32)
            cond = False
            break
        elif palpite == 4:
            print(texto_1)
            print(texto_41)
            print(texto_42)
            print(texto_43)
            cond = False
            break
        elif palpite == 5:
            print(texto_1)
            print(texto_51)
            print(texto_52)
            print(texto_53)
            cond = False
            break
        elif (palpite != 1) or (palpite != 2) or (palpite != 3) or (palpite != 4) or (palpite != 5):
            print('Mas, infelizmente, hoje não é o seu dia de sorte.')
            print('Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.')
            print('Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')
            break
        
    elif (palpite != decimal) and (tentativas >= 0):
        print(f'Resposta incorreta. Mas não desista! Você ainda tem { tentativas } chance(s).')

    elif (palpite != decimal) and (tentativas <= 0):
        if (palpite == 1) or (palpite == 2) or (palpite == 3) or (palpite == 4) or (palpite == 5):
            print('Infelizmente mais uma resposta incorreta.')
            print('Agradecemos sua participação!')
            print('Seu bilhete era premiado. Que pena!')
        else:
            print('Infelizmente mais uma resposta incorreta.')
            print('Agradecemos sua participação!')
            print('Pelo menos seu bilhete não era premiado.')
            print('Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!')
        cond = False