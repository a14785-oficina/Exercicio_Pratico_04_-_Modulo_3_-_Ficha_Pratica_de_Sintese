# INTRODUÇÃO
# Desenvolver um programa em Python que utiliza funções para gerir o stock de materiais escolares de uma escola. O programa deverá permitir o registo, consulta e atualização do stock de forma eficiente.
# PROBLEMA
# A escola necessita de um sistema para gerir o stock de materiais (como canetas, cadernos, borrachas, etc.). Atualmente, o registo é feito manualmente, o que dificulta a atualização e a consulta rápida. Pretende-se um programa que automatize este processo, utilizando funções.
# REQUISITOS
# O programa deve:
# Registar novos materiais no stock.
# Consultar o stock de um material específico.
# Atualizar a quantidade em stock (adição ou remoção).
# Exibir o estado geral do stock.

import time, os, datetime

# Clear screen (cross-platform)
os.system("cls" if os.name == "nt" else "clear")

# ORIENTAÇÕES PARA O DESENVOLVIMENTO
# Passo 1: Criar a Estrutura do Programa
# O programa será composto pelas seguintes funções:

# adicionar_material(): Para registar novos materiais.
# consultar_stock(): Para verificar o stock de um material específico.
# atualizar_stock(): Para adicionar ou remover itens do stock.
# exibir_stock(): Para mostrar o estado geral do stock.

# Passo 2: Implementar o Código
# [ Função para adicionar materiais ao stock ]
def adicionar_material(stock):
    # Regista um novo material no stock.
    nome = input("Nome do material: ").capitalize()
    if nome in stock:
        print("O material já existe no stock!")
    else:
        try:
            quantidade = int(input(f"Quantidade inicial de {nome}: "))
            if quantidade < 0:
                print("Quantidade não pode ser negativa!")
                return
            stock[nome] = quantidade
            print(f"{nome} adicionado com sucesso!")
        except ValueError:
            print("Erro: Quantidade inválida! Deve ser um número inteiro.")

# --- Ínicio do Orginal ---
# def adicionar_material(stock):
#     nome = input("Nome do material: ").capitalize()
#     if nome in stock:
#         print("O material já existe no stock!")
#     else:
#         quantidade = int(input(f"Quantidade inicial de {nome}: "))
#         stock[nome] = quantidade
#         print(f"{nome} adicionado com sucesso!")
# --- Fim do Orginal ---


# [ Função para consultar o stock de um material ]
def consultar_stock(stock):
    # Consulta a quantidade disponível de um material.
    nome = input("Nome do material para consulta: ").capitalize()
    if nome in stock:
        print(f"O stock atual de {nome} é: {stock[nome]}")
    else:
        print(f"{nome} não encontrado no stock.")


# [ Função para atualizar o stock ]
def atualizar_stock(stock):
    # Adiciona ou remove quantidade de um material existente.
    nome = input("Nome do material a atualizar: ").capitalize()
    if nome in stock:
        operacao = input("Deseja adicionar (A) ou remover (R)? ").upper()
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade < 0:
                print("Erro: Quantidade não pode ser negativa!")
                return
            if operacao == "A":
                stock[nome] += quantidade
                print(f"{quantidade} unidade(s) adicionada(s) ao stock de {nome}.")
            elif operacao == "R":
                if quantidade <= stock[nome]:
                    stock[nome] -= quantidade
                    print(f"{quantidade} unidade(s) removida(s) do stock de {nome}.")
                else:
                    print("Quantidade insuficiente em stock!")
            else:
                print("Operação inválida!")
        except ValueError:
            print("Erro: Quantidade inválida! Deve ser um número inteiro.")
    else:
        print(f"{nome} não encontrado no stock.")

# --- Ínicio do Orginal ---
# def atualizar_stock(stock):
#     nome = input("Nome do material a atualizar: ").capitalize()
#     if nome in stock:
#         operacao = input("Deseja adicionar (A) ou remover (R)? ").upper()
#         quantidade = int(input("Quantidade: "))
#         if operacao == "A":
#             stock[nome] += quantidade
#             print(f"{quantidade} unidade(s) adicionada(s) ao stock de {nome}.")
#         elif operacao == "R":
#             if quantidade <= stock[nome]:
#                 stock[nome] -= quantidade
#                 print(f"{quantidade} unidade(s) removida(s) do stock de {nome}.")
#             else:
#                 print("Quantidade insuficiente em stock!")
#         else:
#             print("Operação inválida!")
#     else:
#         print(f"{nome} não encontrado no stock.")
# --- Fim do Orginal ---


# [ Função para exibir o estado geral do stock ]
def exibir_stock(stock):
    # Mostra todos os materiais e suas quantidades.
    print("\nEstado Geral do Stock:")
    print("Material\tQuantidade")
    print("-" * 30)
    if not stock:
        print("Stock vazio.")
    else:
        for material, quantidade in stock.items():
            print(f"{material}\t\t{quantidade}")

# --- Ínicio do Orginal ---
# def exibir_stock(stock):
#     print("\nEstado Geral do Stock:")
#     print("Material\tQuantidade")
#     print("-" * 30)
#     for material, quantidade in stock.items():
#         print(f"{material}\t\t{quantidade}")
# --- Fim do Orginal ---


def file_export(stock):
    # Exporta o stock atual para um ficheiro de texto.
    if not stock:
        print("Stock vazio. Nada para exportar.")
        return

    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y.%m.%d.%H.%M.%S")
    filename = f"{formatted_time}-Stock_Export.txt"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Material\tQuantidade\n")
            file.write("-" * 30 + "\n")
            for material, quantidade in stock.items():
                file.write(f"{material}\t\t{quantidade}\n")
        print(f"Stock exportado com sucesso para: {filename}")
    except IOError:
        print("Erro: Não foi possível criar o ficheiro.")

# [ Função principal para gerir o menu ]
def main():
    stock = {}
    while True:
        menu = '''
        |    Gestão de Stock    |
        |-----------------------|
        | 1. Adicionar Material |
        | 2. Consultar Stock    |
        | 3. Atualizar Stock    |
        | 4. Exibir Stock Geral |
        | 5. Exportar Stock     |
        | 6. Sair               |
        '''
        print(menu)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_material(stock)
        elif opcao == "2":
            consultar_stock(stock)
        elif opcao == "3":
            atualizar_stock(stock)
        elif opcao == "4":
            exibir_stock(stock)
        elif opcao == "5":
            file_export(stock)
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()


# TAREFA PRÁTICA
# Implementa o código no editor Python.
# Adiciona pelo menos 3 materiais ao stock e realiza as seguintes operações:
# Consulta do stock de um material.
# Atualização do stock, adicionando e removendo quantidades.
# Exibição do estado geral do stock.
# Personaliza o programa para incluir uma funcionalidade extra, como a exportação do stock para um ficheiro.


# ENTREGA
# Envia o código desenvolvido( em ficheiro python *.py // 1I-PSI-M3-NumeroAluno-EXPA04.py) e um relatório breve (em formato PDF) explicando como as funções ajudam a organizar o programa.

# Deves publicar o exercício no repositório do GitHub

# Inclui capturas de ecrã com exemplos de execução.
