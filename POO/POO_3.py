class Conta:

    _num_contas = 1

    def __init__ (self, saldo):
        self._numero = Conta.gera_novo_n()
        self._saldo = saldo
        Conta._num_contas +=1

    #Metodo da classe
    @classmethod
    def gera_novo_n(cls):
        novo_n = cls._num_contas * 1234
        return novo_n
    
    def creditar (self, valor):
        self._saldo += valor

    def debitar (self, valor):
        self._saldo -= valor

    @property
    def numero(self):
        return self.numero
    
    @property
    def saldo (self):
        return self._saldo
    
conta_1 = Conta(20)
print ('Conta 1: ', conta_1.__dict__)

conta_2 = Conta(30)
print ('Conta 2: ', conta_2.__dict__)