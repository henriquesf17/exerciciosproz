
# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será
# a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma 2. Subtração 3. Multiplicação 4. Divisão (Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.)

#Codigo

print("""Função para calcular a operação matemática entre dois números.

    Parâmetros:
    O primeiro número.
    O segundo número.
    A operação a ser realizada.
                    1 - Soma
                    2 - Subtração
                    3 - Multiplicação
                    4 - Divisão

    Retorna:O resultado da operação ou 0 se a operação não for válida.""")
    

def calculadora(numero1, numero2, operacao):
    
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

# Uso:
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
op = int(input("Informe o código da operação (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): "))

resultado = calculadora(num1, num2, op)
print("Resultado:", resultado)

