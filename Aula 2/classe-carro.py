class Carro:
    tipo = 'Veículo'
    estados = [ "Desligado", "Ligado" ]
    def __init__(self,marca,modelo,ano,cor,combustivel):
        self.marca = marca
        self.modelo = modelo
        self.ano = int(ano)
        self.cor = cor
        self.estado = self.estados[0]
        self.combustivel = int(combustivel)
    
    def pintar(self,novacor):
        print(f"Pintando o carro {self.cor} com a nova cor {novacor}.")
        self.cor = novacor
    
    def ligar(self):
        print("Ligando o carro...")

        if self.estado != self.estados[1]:    
            if self.combustivel > 0:
                self.estado = self.estados[1]
                print(f'O carro está {self.estado}')
            else:
                print("O carro não tem combustível para ligar.")
        else:
            print("O carro já estava ligado!")
    
    def desligar(self):
        print("Desligando o carro...")
        self.estado = self.estados[0]
        print(f'O carro está {self.estado}')
    
    def abastecer(self,combustivel):
        self.combustivel += combustivel
        print(f"Agora temos {self.combustivel} litros de combustível no tanque do carro.")

    def __str__(self):
        return(self.marca + ' ' + self.modelo + ' ' + str(self.ano) + ' ' + self.cor + ' ' + str(self.combustivel) + ' Litros no tanque.')

def criaListaCarros(quantidade):
    print()
    carros = list()
    for i in range(quantidade):
        marca = input(f"Qual é a marca do carro {i+1}?: ")
        modelo = input(f"Qual é o modelo do carro {i+1}?: ")
        ano = input(f"Qual é o ano do carro {i+1}?: ")
        cor = input(f"Qual é a cor do carro {i+1}?: ")
        combustivel = input(f"Quantos litros de combustível tem no tanque do carro {i+1}?: ")
        carros.append(Carro(marca,modelo,ano,cor,combustivel))
    return(carros)

lCarros = criaListaCarros(2)

for carro in lCarros:
    print()
    print(carro)
    carro.ligar()
    carro.ligar()
    carro.desligar()
    carro.pintar('azul')
    carro.abastecer(10)
    print(carro)
    