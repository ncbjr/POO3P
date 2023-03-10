class Conta:
    def __init__(self,cod,titular,saldo,limite):
        self.cod = cod
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        print('Nome do escopo',__name__)
    
    def Exibir(self):
        print(f'Conta: {self.cod}\nTitular: {self.titular}\nSaldo: {self.saldo}\nLimite: {self.limite}')
    
    def Deposita(self,valor):
        self.saldo += valor
    
    def Saque(self,valor):
        self.saldo -= valor
        input("Retire o dinheiro na abertura abaixo.")
    
    def Extrato(self):
        print(f'O saldo da conta é: {self.saldo}')
