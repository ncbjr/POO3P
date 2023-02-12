#3 - criar uma função que vai receber algumas cidades(5)
#Organizar em ordem alfabética
cidades = list()

for i in range(1,6):
    print("Insira a cidade",i,": ",end='')
    cidades.append(input())

bagunca = cidades

for a in range(len(bagunca)-1):
    for b in range(len(bagunca)-1):
        if bagunca[b] > bagunca[b+1]:
            tmp=bagunca[b]
            bagunca[b] = bagunca[b+1]
            bagunca[b+1] = tmp

print()
for nome in bagunca:
    print(nome)