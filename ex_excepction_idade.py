"""Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido."""

def obter_nome():
    return input("Digite seu nome completo: ")

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite seu ano de nascimento (entre 1922 e 2023): "))
            if 1922 <= ano <= 2023:
                return ano
            else:
                print("Ano inválido. Por favor, insira um ano entre 1922 e 2023.")
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

def calcular_idade(ano_nascimento, ano_atual=2024):

    return ano_atual - ano_nascimento

# Código principal 
nome = obter_nome()
ano_nascimento = obter_ano_nascimento()
idade = calcular_idade(ano_nascimento)

print(f"{nome}, você completou ou completará {idade} anos em 2022.")