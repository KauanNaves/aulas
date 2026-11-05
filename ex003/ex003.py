class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos.
    """
    def __init__(self, id:int , titular:str, saldo:float = 0):
        self.id = id
        self.titular = titular 
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso, saldo atual de R${self.saldo:,.2f}")


    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f}"


    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}!")
            return
        else:
            print("Valor inválido para depósito")


    def sacar(self, valor: float):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")
            return
        else:
            print("Saldo insuficiente!")
    

conta1 = ContaBancaria(112, "Kauan", 5856)
conta1.depositar(1000)
print(conta1)