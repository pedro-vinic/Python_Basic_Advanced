"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re
import sys
import random

cpf = ""

for i in range(9):
    cpf += str(random.randint(0,9))

cpf_enviado = cpf

entrada_sequencial = cpf == cpf[0] * len(cpf)

if entrada_sequencial:
    print("Você digitou número sequênciais.")
    sys.exit()

nove_digitos = cpf_enviado[:9]

contador_regressivo_1 = int(10)

resultado_1 = 0

for digito in nove_digitos:
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -=1

digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


dez_digitos = nove_digitos + str(digito_1)

contador_regressivo_2 = 11

resultado_2 = 0

for digito in dez_digitos:
    resultado_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -=1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_calculado = f"{nove_digitos}{digito_1}{digito_2}"

print(cpf_calculado)
