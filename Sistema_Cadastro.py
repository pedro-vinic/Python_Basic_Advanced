"""
Sitema de cadastro e de consulta. Utilizando fuções
com argumentos nomeados e posicionais, valores padrões e escopos de módulos.
"""

usuarios = []
tecnicos = []

def cadastro_usuario (nome, telefone, *args, tipo= 'Usuário'):
    print("Sistema de cadastro de usuário.")
    return {'Tipo': tipo, 'Nome': nome, 'Telefone': telefone, 'Info_Adcional': [*args]}

def cadastro_tecnico (nome, telefone, profissao, *args, tipo= 'Tecnico'):
    print("Sistema de cadastro de tecnico.")
    return {'Tipo': tipo, 'Nome': nome, 'Telefone': telefone, 'Profissão': profissao, 'Info_Adcional': [*args]}

def exibir_usuarios (lista):
    if not lista:
        print('Usuarios não encontrados.')

    else:
        for usuario in lista:
            print(f"Tipo: {usuario['Tipo']}, Nome: {usuario['Nome']}, Telefone: {usuario['Telefone']}, Outros Contatos: {usuario['Info_Adcional']}")

def exibir_tecnicos (lista):
    if not lista:
        print('Tecnicos não encontrados.')

    else:
        for tecnico in lista:
            print(f"Tipo: {tecnico['Tipo']}, Nome: {tecnico['Nome']}, Telefone: {tecnico['Telefone']}, Outros Contatos: {tecnico['Info_Adcional']}")  

def menu():
    while True:
        opcoes = input("""
        Sistema de Cadastro

        [u] Cadastro de Usuário
        [t] Cadastro de Tecnico
        [lu] Lista de Usuários
        [lt] Lista de Tecnicos
        [f] Finalizar

        >>> """)

        print()
        print(f"Opção escolhida: {opcoes}")

        if opcoes == 'u':
            nome = input('Digite seu nome: ')
            telefone = input('Digite seu telefone: ')
            email = input('Digite seu email: ')
            outro_telefone = input('Digite outro telefone: ')
            usuario = cadastro_usuario(nome, telefone, email, outro_telefone)
            usuarios.append(usuario)
            print('Usuário cadastrado com sucesso!')
        
        elif opcoes == 't':
            nome = input('Digite seu nome: ')
            telefone = input('Digite seu telefone: ')
            profissao = input('Digite sua profissão: ')
            email = input('Digite seu email: ')
            outro_telefone = input('Digite outro telefone: ')
            tecnico = cadastro_tecnico(nome, telefone, profissao, email, outro_telefone)
            tecnicos.append(tecnico)
            print('Tecnico cadastrado com sucesso!')

        elif opcoes == 'lu':
            print('Lista de usuários')
            exibir_usuarios(usuarios)

        elif opcoes == 'lt':
            print('Lista de tecnicos.')
            exibir_tecnicos(tecnicos)

        elif opcoes == 'f':
            print('Programa finalizado!')
            break

        else:
            print('Opção inválida! Tente novamente.')

menu()
