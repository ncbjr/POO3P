#2 Criar duas listas de números inteiros e mesclá-las em uma terceira lista em ordem crescente.
import ex1

lista1 = ex1.main()
lista2 = ex1.main()
lista3 = list()

lista3 = lista1 + lista2
lista3.sort()
print(lista3)