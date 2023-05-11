from Pessoas import *

nomes = [ 'Leandro', 'Cristiano', 'Nilton']
idades = [ 75, 30, 25]
cpfs = [ '14789632158', '12369874125', '14569852367' ]
salarios = [ 15000, 7000, 6000]

funcionarios = list()

funcionarios.append(Gerente(nomes[0],idades[0],cpfs[0],salarios[0]))
funcionarios.append(Coordenador(nomes[1],idades[1],cpfs[1],salarios[1]))
funcionarios.append(Analista(nomes[2],idades[2],cpfs[2],salarios[2]))

for funcionario in funcionarios:
    print(funcionario.nome,type(funcionario),funcionario.salario,funcionario.calculaBonus())