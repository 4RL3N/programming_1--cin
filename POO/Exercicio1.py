class Conta:
    def __init__ (self, numero, saldo, limite):
        self._numero = numero
        self._saldo = saldo
        self._limite = limite
        self.saldo_disp = saldo + limite

    def creditar(self, valor):
        self._saldo += valor
        
    def debitar(self, valor):
        self._saldo -= valor

    @property #Leitura do atributo numero
    def numero(self):
        return self._numero
    
    @property #Leitura do atributo Saldo
    def saldo(self):
        return self._saldo
    
    @property
    def limite(self):
        return self.limite
    
    @limite.setter
    def limite(self, limite):
        if (limite < 0):
            print('Limite não pode ser negativo.')
        else:
            self._limite = limite

    @limite.deleter
    def limite(self):
        del self._limite

conta_a = Conta("123-a", 0.0, 0.0)
conta_b = Conta("123-b", 0.0, 0.0)
conta_c = Conta("123-c", 0.0, 0.0)

conta_a.creditar(15.0)
conta_b.creditar(30.0)

print("Conta a:", conta_a.__dict__)
print("Conta b:", conta_b.__dict__)
print("Conta c:", conta_c.__dict__)
print("---------------------------")

conta_c.creditar(conta_a.saldo + conta_b.saldo)
conta_a.debitar(conta_a.saldo)
conta_b.debitar(conta_b.saldo)

del conta_a.limite
del conta_b.limite
conta_c.limite = 10000.0

print("Conta a:", conta_a.__dict__)
print("Conta b:", conta_b.__dict__)
print("Conta c:", conta_c.__dict__)