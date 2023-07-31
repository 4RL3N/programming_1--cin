frase = str(input('Digite aqui: '))
dinheiro_total = 0.0
protetor = False
clima = True
if frase == 'separar dinheiro':
    dinheiro_a_mais = float(input('Digite o dinheiro: '))
    dinheiro_total += dinheiro_a_mais
if frase == 'passar protetor':
    protetor = True
if frase == 'choveu':
    clima = False
if frase == 'parou de chover':
    clima = True

while not frase == 'ir para a praia':
    frase = str(input('Digite, while: '))
    if frase == 'separar dinheiro':
        dinheiro_a_mais = float(input('Digite o dinheiro: '))
        dinheiro_total += dinheiro_a_mais
    if frase == 'passar protetor':
        protetor = True
    if frase == 'choveu':
        clima = False
    if frase == 'parou de chover':
        clima = True
    
else:
    if clima == False:
        print('Hoje não vai dar pra ir, chuvinha barrou')
    elif clima == True:
        print('Hoje tem sol e mar!')
        if protetor == False and dinheiro_total <10.0:
            print('Você não chegou muito bem, chame um médico!')
        elif protetor == False and dinheiro_total >=10.0:
            print('O novo camarão do CIn foi criado')
        elif protetor == True and dinheiro_total <10.0:
            print('Só faltou uma aguinha de coco...')
        elif protetor == True and dinheiro_total >=10:
            print('Aí sim! Hoje rendeu!')