# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

import os

print("Passe cinco números!")

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero

    os.system("cls")    
    print("O resultado é: ", total)
    
argumentos = ()

for i in range(5):
    numero = int(input("Informe o valor: "))
    argumentos += (numero,)


multiplicar(*argumentos)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

import os

print("Verifique se o número é par ou ímpar!")

def verficacao(numero):
        
    resultado = numero % 2
    
    if resultado == 0:
        return "par"
    
    else:
        return "ímpar"
           

numero = int(input("Digite: "))


os.system("cls")
print(f' O número {numero} é {verficacao(numero)}.')





        
        


