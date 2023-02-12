#2 - criar um programa para organizar um array(lista/tupla)
#-> por ordem alfabética = NÂO PODE USAR O SORT SORTED e AFINS
#NÂO PODE USAR FUNÇÂO PRONTA DO PYTHON

bagunca = [ "zorinos", "debian", "centos", "ubuntu", "mx", "mint" ]

for a in range(len(bagunca)-1):
    for b in range(len(bagunca)-1):
        if bagunca[b] > bagunca[b+1]:
            tmp=bagunca[b]
            bagunca[b] = bagunca[b+1]
            bagunca[b+1] = tmp

for nome in bagunca:
    print(nome)