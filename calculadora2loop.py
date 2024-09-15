def calculadora(numero1, numero2, operacao):
    """
    Função para calcular a operação matemática entre dois números.

    Parâmetros:
    numero1 (float): O primeiro número.
    numero2 (float): O segundo número.
    operacao (int): Código da operação a ser realizada.
                    1 - Soma
                    2 - Subtração
                    3 - Multiplicação
                    4 - Divisão

    Retorna:
    float: O resultado da operação ou 0 se a operação não for válida.
    """
    if operacao == 1:
        return numero1 + numero2
    elif operacao == 2:
        return numero1 - numero2
    elif operacao == 3:
        return numero1 * numero2
    elif operacao == 4:
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: Divisão por zero"
    else:
        return 0

def menu():
    """
    Função para exibir o menu de opções.
    """
    print("Escolha uma operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

def main():
    """
    Função principal que controla o fluxo do programa.
    """
    while True:
        menu()  # Exibe o menu de opções
        operacao = int(input("Digite o número para a operação correspondente: "))

        if operacao == 0:
            print("Saindo do programa...")
            break

        if operacao in [1, 2, 3, 4]:
            try:
                numero1 = float(input("Informe o primeiro número: "))
                numero2 = float(input("Informe o segundo número: "))
                resultado = calculadora(numero1, numero2, operacao)
                if operacao == 4 and numero2 == 0:
                    print(resultado)  # Exibe a mensagem de erro para divisão por zero
                else:
                    print("Resultado:", resultado)
            except ValueError:
                print("Por favor, insira um número válido.")
        else:
            print("Essa opção não existe.")

if __name__ == "__main__":
    main()