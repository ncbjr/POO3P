import classCliente

# Exemplo de uso:
cliente1 = Cliente('João')
cliente2 = Cliente('Maria')

conta1 = Conta(cliente1, 1000, 500)
conta2 = Conta(cliente2, 500, 0)

conta1.depositar(200)
conta1.sacar(300)
conta1.transferir(conta2, 500)

print(f"Saldo da conta de {cliente1.nome}: R$ {conta1.saldo:.2f}")
print(f"Saldo da conta de {cliente2.nome}: R$ {conta2.saldo:.2f}")

for transacao in conta1.historico.transacoes:
    print(transacao)

for transacao in conta2.historico.transacoes:
    print(transacao)





from classCliente import Cliente
from classConta import *

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
