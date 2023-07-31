class Conta:
    def __init__(self, numero, saldo):
        self._numero = numero #o self cria uma variavel com o nome numero com o valor do parametro dado na função
        self._saldo = saldo #quando tem "_" antes do nome do atributo, é privado

    def creditar(self, valor):
        self._saldo += valor

    def debitar(self, valor):
        self._saldo -= valor

conta = Conta('123-x', 0.00)
condicao = True

while condicao:
    entrada, valor = input().split(" ")
    valor = int(valor)

    if entrada == "Creditar":
        conta.creditar(valor)

    elif entrada == "Debitar":
        conta.debitar(valor)
        
    else:
        break

    print("#########")
    print('Número: ',conta._numero)
    print('Saldo: ',conta._saldo)
    print("#########")