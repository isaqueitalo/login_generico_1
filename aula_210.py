class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # def metodo_de_classe(self):
        # print('hey')
    @classmethod    
    def metodo_de_classe(cls):
        print('hey')

    @classmethod    
    def criar_com_50(cls, nome):
        return cls(nome, 50)
    
    @classmethod    
    def criar_anonimo(cls, idade):
        return cls('anonima', idade)
    


p1 = Pessoa('joão', 34)
p2 = Pessoa.criar_com_50('helena')
p3 = Pessoa.criar_anonimo(23)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

#p1.metodo_de_classe()
print(Pessoa.ano)
Pessoa.metodo_de_classe()


class Class:

    @staticmethod
    def method(*args, **kwargs):
        print('Hey static', args, kwargs)

p1 = Class()
p1.method(1, 2, 3)
Class.method(nomeado='valor')
