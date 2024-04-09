# Exercício - sistema de perguntas e respostas

'''Aqui eu defini a função de imprimir as perguntas e respostas.
        E de coletar a reposta do usúario e puxei a função que criei para verificar
        as respostas com parâmetros  resposta e resposta correta.
        Junto coloquei um contador para registrar quantidades de erros e acertos.'''


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': {'a': 1, 'b': 3, 'c': 4, 'd': 5},
        'Resposta': 4,
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': {'a': 25, 'b': 55, 'c': 10, 'd': 51},
        'Resposta': 25,
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': {'a': 4, 'b': 5, 'c': 2, 'd': 1},
        'Resposta': 5,
    },
]

def questao():
    
    for pergunta in perguntas:
        print(f'Pergunta: {pergunta["Pergunta"]}')
        print(' ')
    
        for i, (chave, opcao) in enumerate(pergunta['Opções'].items()):
            print(f'{chave}) {opcao}')
            print(' ')


        resposta_usuario = input('Resposta: ')

        verificar_resposta(resposta_usuario, pergunta['Resposta'])


def verificar_resposta(resposta, resposta_correta):
    global contador_acertos, contador_erros
    contador_acertos = 0
    contador_erros = 0    

    if int(resposta) == resposta_correta:
        print('A sua resposta está certa.')
        print('\n')
        contador_acertos += 1

    else:
        print('A sua resposta está errada.')
        print('\n')
        contador_erros += 1

    
questao()

print(f'Você acertou {contador_acertos} perguntas e errou {contador_erros}!')

