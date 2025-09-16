# Escopo da classe e de métodos de classe
class Animal:
    #nome = 'animal'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def acao(self):
        return f'{self.nome} esta executando uma ação'

leao = Animal('Leao')
print(leao.nome)
print(leao.acao())