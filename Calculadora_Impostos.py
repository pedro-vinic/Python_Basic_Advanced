"""Aqui o intuito foi exercitar closure e função que retorna outra função."""

from time import sleep 

def calcular_imposto(aliquota):
    def valor(receita):
        return receita * (aliquota / 100)
    return valor

impostos = {
    'Imposto Municipal': calcular_imposto(5),
    'Imposto Estadual': calcular_imposto(10),
    'Imposto Nacional': calcular_imposto(15)
}
  
print("Calculadora de impostos!")
print()
valor_receita = int(input("Digite o valor da sua receita: "))
print()
print("Calculando...")

for i in range(10):
    print(':' * (i + 1), end='\r')
    sleep(0.5)

for nome, funcao_imposto in impostos.items():
    print(f'{nome}: R${funcao_imposto(valor_receita):.2f}')
