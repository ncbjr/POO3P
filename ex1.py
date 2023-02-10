#1 - cálculo de média de 4 notas => 7 aprovado
#<7 >= 4 = Exame final <4 reprovado

notas = []
media = 0

for i in range(1,5):
    print("Insira a nota",i,": ")
    media += (float(input())) / 4

if media >= 7:
    print("Aprovado.")
elif media < 4:
    print("Reprovado.")
else:
    print("\nExame final.")