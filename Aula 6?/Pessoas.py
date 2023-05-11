#Classe mãe
class Pessoa():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

#Classe filha
class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)

#Classe filha
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, salario,bonus=0):
        super().__init__(nome, idade, cpf)
        self.bonus = bonus
        self.salario = salario
    
    def calculaBonus(self):
        return(self.salario*self.bonus)

#Classe neta
class Gerente(Funcionario):
    def __init__(self,nome,idade,cpf,salario):
        super().__init__(nome,idade,cpf,salario,bonus=0.9)

#Classe neta
class Coordenador(Funcionario):
    def __init__(self,nome,idade,cpf,salario):
        super().__init__(nome,idade,cpf,salario,bonus=0.5)

#Classe neta
class Analista(Funcionario):
    def __init__(self,nome,idade,cpf,salario):
        super().__init__(nome,idade,cpf,salario,bonus=0.2)
