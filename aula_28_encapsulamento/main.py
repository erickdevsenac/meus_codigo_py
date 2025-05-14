class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0
        
    def depositar(self, valor):
        self._saldo += valor
        return self._saldo
        
    def sacar(self, valor):
        if(self._saldo >= valor):
            self._saldo -= valor
            return self._saldo
        else:
            return f'Saldo insuficiente! {self._saldo}'
        
    def extrato(self):
        return f'A conta do {self.titular} possui {self._saldo} R$.'



class ContaCorrente(ContaBancaria):
    def __init__(self, titular):
        super().__init__(titular)
        self.__limite = 200
        self._saldo += self.__limite 
        
    def sacar(self, valor):
        if(self._saldo < valor):
            return f'Saldo insuficiente! {self._saldo}'
        else:
            return self._saldo - valor
            
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular):
        super().__init__(titular)       
    
    
conta_erickson = ContaCorrente('Erickson')
print(conta_erickson.extrato())
conta_erickson.depositar(500)
print(conta_erickson.extrato())
print(conta_erickson.sacar(700))

# conta1 = ContaBancaria('Erickson')
# print(conta1.extrato())

# conta1.depositar(10000.90)
# print(conta1.extrato())

# print(conta1.sacar(20000))
# print(conta1.sacar(10.9))
# print(conta1.extrato())


# print(conta1._saldo)
# print(f'A conta do {conta1.titular} possui {conta1.saldo} R$.')

# conta1.saldo = -900
# print(f'A conta do {conta1.titular} possui {conta1.saldo} R$.')
        