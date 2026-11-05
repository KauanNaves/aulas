# Declaração de Classe
class Gafanhoto:
    """
Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use
variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome:str = "", idade:int = 0): # Método construtor
        # Atributos de instância
        self.nome = nome
        self.idade = idade

    # Métodos de instância
    def aniversario(self):
        self.idade += 1


    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


    def __getstate__(self):
        return f"Estado: nome={self.nome} ; idade={self.idade}"

# Declaração de Objetos
g1 = Gafanhoto("Kauan", 21)
g2 = Gafanhoto("Cecília", 20)
g3 = Gafanhoto("Victor", 14)

print(g1)
print(g2)
print(g3)

print()

print(g1.__doc__) # Dunder Attributes
print(g1)
print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method

print()

print(g2)
print(g2.__dict__)
print(g2.__getstate__())
print(g2.__class__)