# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def calcular(num):
    def duplicar():
        return f"O duplo de {num} é {num * 2}!"
    
    def triplicar():
        return f"O triplo de {num} é {num * 3}!"
    
    def quadruplicar():
        return f"O quadruplo de {num} é {num * 4}!"

    return duplicar(), triplicar(), quadruplicar()
    

num = int(input("Digite um número: "))

mensagem = calcular(num)

for texto in mensagem:
    print(texto)

    