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
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'O seu novo saldo é: {self.saldo}')
            return True
        else:
            print(f'Não vai rolar! Seu saldo é: {self.saldo}')
            return False
    def Extrato(self):
        print(f'O saldo da conta {self.cod} é: {self.saldo}')

    def Transfere(self,destino,valor):
        if self.Saque(valor):
            destino.Deposita(valor)
        print(self.saldo)