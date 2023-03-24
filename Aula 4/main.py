from cliente import Cliente
from ClassConta import *

if __name__ == '__main__':    
    cliente1 = Cliente('Nilton','Junior','17754327775')
    conta1 = Conta('123-5',cliente1,100,5000)
    
    cliente2 = Cliente('Marcos','Antônio','18616111919')
    conta2 = Conta('133-5',cliente2,500,5000)
    
    for conta in [ conta1, conta2 ]:
        print("\nExtrato da conta de {}".format(conta.titular.nome))
        print("Saldo atual: {}\n".format(conta.saldo))
        conta.historico.imprime()

    conta1.Transfere(conta2,50)

    for conta in [ conta1, conta2 ]:
        print()
        conta.historico.imprime()
