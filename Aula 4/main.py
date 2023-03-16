from ClassConta import *

if __name__ == '__main__':    
    conta = Conta('123-5','Nilton Junior',100,5000)
    conta2 = Conta('124-5','Nilton Braga',80,5000)
    print(conta.saldo)
    print(conta2.saldo)
    conta.Transfere(conta2,50)
    print(conta.saldo)
    print(conta2.saldo)

"""
    conta.Exibir()
    conta.Deposita(100)
    conta.Extrato()
    conta.Saque(300)
    conta.Extrato()
"""