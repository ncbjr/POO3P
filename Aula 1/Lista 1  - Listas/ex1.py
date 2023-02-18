#1 Criar uma lista com 10 números inteiros aleatórios e imprimir o maior e o menor número da lista.
def main ():
    import random
    
    lista = list()
    for i in range(10):
        lista.append(random.randint(0, 100))

    print("Maior: ",max(lista))
    print("Menor: ",min(lista))

    return(lista)

if __name__ == '__main__':
    main()