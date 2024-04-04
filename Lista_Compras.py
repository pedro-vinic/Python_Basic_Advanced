"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import copy
import os

lista_compras = list()


while True:

    def desejo_continuar():

        retorno = input(
            """Deseja retorna ao menu incial?\n
            [S] Sim.
            [N] Não.
            >>>> """).upper()
                
        if retorno == "S":
            pass

        elif retorno == "N":
            print("Até logo!")
            quit()
                                
        else:
            print("Opção digitada é inválida! Tente novamente.")
            desejo_continuar()


    interacao_lista_compras = input(
    """Escolhe o que deseja fazer.\n
    [1] Inserir\n
    [2] Excluir\n
    [3] Listar\n
    >>>> """)


    if interacao_lista_compras == "1":
        qntd_lista = input("""
        Quantos itens deseja adicionar?\n
        >>>> """) 

        try:
            int_qntd_lista = int(qntd_lista)
        
        except ValueError:
            os.system("cls")
            print("O valor digitado é inválido! Tente novamente.")
            continue

                
        if int_qntd_lista >= 1:
            for item in range(1, int_qntd_lista + 1):
                itens_lista = input(f"""
                {item} item: """)
                lista_compras.append(itens_lista)

        
        desejo_continuar()


    elif interacao_lista_compras == "2":
        for i, item in enumerate(lista_compras, start=1):
            print(f"{i} - {item}")

        item_exclui = int(input("Digite o número do item que deseja excluir: "))

        if 1 <= int(item_exclui) <= len(lista_compras):
            del lista_compras[item_exclui - 1]

        desejo_continuar()



    elif interacao_lista_compras == "3":
        print("Minha lista de compras:")
        for i, item in enumerate(lista_compras, start=1):
            print(f"""
            {i} - {item}           
            """)
            
        desejo_continuar()
        

    else:
        os.system("cls")
        print("O valor digitado é inválido! Tente novamente.")
        continue  
                
   

    
        
                
            
    