#Uma forma de criar dicionários.
import os
import copy

pessoa = {}

pessoa['nome'] = 'Pedro'
pessoa['sobrenome'] = 'Senna'
pessoa['idade'] = 25

print(pessoa) #Imprimindo dicionário
print(pessoa['sobrenome']) #Acessando uma dhave do dict

del pessoa['idade'] #Deletando uma chave

print(pessoa)

if pessoa.get('idade') is not None: #O None retorna um valor que não é válido. Não encontrou idade.
    print("Existe")

else:
    print("Não existe!")


if pessoa.get('nome') is None: 
    print('Não existe')

else:
    print('Existe')

print(list(pessoa.keys())) #Acessando as chaves do dict
print(list(pessoa.values())) #Acessando os valores do dict

for chave, valor in pessoa.items(): #O Items funciona como o enumerate. Retorna chave e valor em variáveis separadas.
    print(f'{chave}: {valor}')

pessoa.setdefault('idade', 25) #Ele adiciona uma chave e um valor no dict
print(pessoa['idade'])

os.system('cls')

d1 = {
    'a': 1,
    'b': 2,
    'li': [0, 1, 2, 3]
}

#d2 = d1.copy() Retorna uma cópia rasa (shallow copy)

d2 = copy.deepcopy(d1) #Retorna uma cópia profunda, de todos os níveis do dict (deep copy)

d2['a'] = 54
d2['li'][1] = 9999999
print(d1)
print(d2)

os.system('cls')


cliente = {
    'nome': 'Pedro',
    'sobrenome': 'Senna',
}

name = cliente.pop('nome') #Retira um item da dict e guarda numa variável

print(name)
print(cliente)

print(cliente.get('nome', 'não existe'))

os.system('cls')


cliente = {
    'nome': 'Pedro',
    'sobrenome': 'Senna',
}

ultima_chave = cliente.popitem() #Retira o último item da dict e guarda numa variável

print(ultima_chave)
print(cliente)

print(cliente.get('sobrenome', 'não existe'))

os.system('cls')


cliente = {
    'nome': 'Pedro',
    'sobrenome': 'Senna',
}

cliente.update(nome='Guilherme', sobrenome='Gameleiro') #Update altera o valor do dict

print(cliente)




