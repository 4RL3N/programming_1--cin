class Poupanca:

    _num_contas = 1

    def __init__ (self, saldo, taxa_juros):
        self._numero = Poupanca.gera_novo_numero()
        self._saldo = saldo
        self._taxa_juros = taxa_juros
        Poupanca._num_contas += 1

    @classmethod
    def gera_novo_numero(cls):
        novo_numero = cls._num_contas * 1234
        return novo_numero
        
    @classmethod
    def get_num_contas(cls):
        return cls._num_contas * 1234
        
    # Método
    def render_juros(self):
        self.creditar(self._saldo * self._taxa_juros)

    def creditar(self, valor):
        self._saldo += valor

    def debitar(self, valor):
        self._saldo -= valor
        
    @property
    def numero(self):
        return self._numero
        
    @property
    def saldo(self):
        return self._saldo
        
    @property
    def taxa_juros(self):
        return self._taxa_juros
        
    @taxa_juros.setter
    def taxa_juros(self, taxa_juros):
        self.taxa_juros = taxa_juros

#Testando
conta_poupança = Poupanca(0.0, 0.01)
conta_poupança.creditar(200.0)
conta_poupança.render_juros()
print(conta_poupança.__dict__)
print(help(Poupanca))