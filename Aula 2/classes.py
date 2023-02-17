class Pessoa:
    especie = 'humano'
    def __init__(self,nome,relacao,idade):
        self.nome = nome
        self.relacao = relacao
        self.idade = int(idade)
    def __str__(self):
        return(self.nome + ' ' + self.relacao + ' ' + str(self.idade) + ' ' + self.especie)
    
    def trocanome(self,novonome):
        self.nome = str(novonome)
    
    def dobraidade(self):
        self.idade = self.idade * 2 

a = Pessoa('Nilton','Aluno',24)

print(a)
a.trocanome('Thiago')
a.dobraidade()
print(a)