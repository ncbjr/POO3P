from datetime import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.today()
        self.transacoes = list()

    def imprime(self):
        print(f'Data de abertura: {self.data_abertura}')
        for transacao in self.transacoes:
            print(f'{transacao}')