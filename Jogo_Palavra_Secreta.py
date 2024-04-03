"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = "bicicleta"

letras_acertadas = ""

palavras_sugeridas = ""

i = 0

while True:

    sugestao_palavra = input("Digite uma letra para descobrir a palavra secreta: ")

    if len(sugestao_palavra) > 1:
        print("Digite apenas uma letra!")
        continue

    elif sugestao_palavra == "":
        print("Você não digitou uma letra! Tente novamente.")
        continue

    elif sugestao_palavra not in palavras_sugeridas:
        palavras_sugeridas += sugestao_palavra

    else:
        print("Você já deu essa sugestão! Tente novamente.")
        continue

    if sugestao_palavra in palavra_secreta:
        i += 1
        letras_acertadas += sugestao_palavra
    
    palavra_formada = ""
    
    for sugestao_palavra in palavra_secreta:

        if sugestao_palavra in letras_acertadas:
            palavra_formada += sugestao_palavra
        
        else:
            palavra_formada += "*"  

    print("Palavra formada: ", palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("cls")
        print("Parabéns! Você descobriu a palavra secreta.")
        print(f"O índice de tentavivas foi de {i}x.")
        break