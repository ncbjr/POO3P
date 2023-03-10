from ClassConta import *

if __name__ == '__main__':    
    conta = Conta('123-5','Nilton Junior',100,5000)
    conta.Exibir()
    conta.Deposita(100)
    conta.Extrato()
    conta.Saque(300)
    conta.Extrato()
