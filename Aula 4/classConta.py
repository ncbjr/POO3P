from classExtrato import Historico

class Conta:
    def __init__(self,cliente,saldo=0,limiteEspecial=100):
        self.__titular = cliente
        self.__saldo = saldo
        self.__limite = limiteEspecial
        self.__historico = Historico()

    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @property
    def historico(self):
        return self.__historico

######################################################
    
    @saldo.setter
    def saldo(self,valor):
        if valor < (self.limite) < 0:
            print('Não é possível ter saldo negativo além do limite especial.')
        self.__saldo = valor

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