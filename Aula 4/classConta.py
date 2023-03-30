from classExtrato import Extrato

class Conta:
    def __init__(self,cod,titular,saldo,limite):
        self.cod = cod
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Extrato()

    def Exibir(self):
        print(f'Conta: {self.cod}\nTitular: {self.titular}\nSaldo: {self.saldo}\nLimite: {self.limite}')
    
    def Deposita(self,valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito de {}".format(valor))
    
    def Saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'O seu novo saldo é: {self.saldo}')
            self.historico.transacoes.append("saque de {}".format(valor))
            return True
        else:
            print(f'Não vai rolar! Seu saldo é: {self.saldo}')
            return False
    def Extrato(self):
        print(f'O saldo da conta {self.cod} é: {self.saldo}')

    def Transfere(self,destino,valor):
        if self.Saque(valor):
            destino.Deposita(valor)
            self.historico.transacoes.append("tranferência de {} para {} no valor de: {}".format(self.titular.nome, destino.titular.nome,valor))
            destino.historico.transacoes.append("tranferência de {} para {} no valor de: {}".format(self.titular.nome, destino.titular.nome,valor))

        print(self.saldo)