from datetime import datetime

class Historico:
    def __init__(self):
        self.__transacoes = list()

    @property
    def transacoes(self):
        return self.__transacoes
    
    def imprime(self):
        for transacao in self.transacoes:
            print(f'{transacao}')
    
    def registrarTransacao(self, transacao):
        self.transacoes.append(datetime.today() + ' - ' + transacao)