class Conta:
    def __init__(self, numero, saldo, limite):
        self.numero = numero #o self cria uma variavel com o nome numero com o valor do parametro dado na função
        self.saldo = saldo #quando tem "_" antes do nome do atributo, é privado
        self.limite = limite
    
    @property
    def saldo_disp(self):
        return self.saldo + self.limite
    
conta = Conta("4RL3N", 100.0, 0.0)
print(f'Saldo..........:', conta.saldo)
print(f'Limite.........:', conta.limite)
print(f'Saldo disponível..:' , conta.saldo_disp)
print('------------------------')

conta.limite = 1000000.0
print(f'Saldo..........:', conta.saldo)
print(f'Limite.........:', conta.limite)
print(f'Saldo disponível..:' , conta.saldo_disp)
