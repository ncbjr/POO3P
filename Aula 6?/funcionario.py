class Pessoa():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf):
        pass

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, salario):
        super().__init__(nome, idade, cpf)
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self,nome,idade,cpf,salario):
        super().__init__(nome,idade,cpf,salario)

class Coordenador(Funcionario):
    def __init__(self,nome,idade,cpf,salario):
        super().__init__(nome,idade,cpf,salario)

class Analista(Funcionario):
    def __init__(self,nome,idade,cpf,salario):
        super().__init__(nome,idade,cpf,salario)
