# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = ""
        self.idade = 0

    # Métodos de instância
    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Kauan"
g1.idade = 21

g2 = Gafanhoto()
g2.nome = "Cecília"
g2.idade = 20

g3 = Gafanhoto()
g3.nome = "Victor"
g3.idade = 14

print(g1.mensagem())
print(g2.mensagem())
print(g3.mensagem())