import json

from aula_208_a_ import CAMINHO_ARQUIVO, Pessoa


# fazer_dump()
with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:


    pessoas = json.load(arquivo)

    pessoa_1 = Pessoa(**pessoas[0])
    pessoa_2 = Pessoa(**pessoas[1])
    
    
print(pessoa_1.nome)
print(pessoa_2.nome)











    