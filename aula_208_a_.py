import json

CAMINHO_ARQUIVO = 'aula_208.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando instâncias da classe Pessoa
pessoa_1 = Pessoa('joão', 33)
pessoa_2 = Pessoa('helena', 33)
pessoa_3 = Pessoa('joana', 33)

# Convertendo objetos em dicionários
bd = [vars(pessoa) for pessoa in [pessoa_1, pessoa_2, pessoa_3]]

# Salvando no arquivo JSON
with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
