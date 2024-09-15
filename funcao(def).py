#João precisa calcular seu Índice de Massa Corporal (IMC) para avaliar seu peso ideal. Sabendo que a fórmula para calcular o IMC é:
# peso ÷ altura², crie um programa que calcule e informe a classificação do IMC.

print("Informe o peso (em kg):")
peso = float(input())  

print("Informe a altura (em cm):")
altura = float(input())  

def calculadoraImc(peso, altura):

     imc = peso/(altura*altura) * 10000

     if (imc <= 18.5): return "Magreza"

     elif (imc > 18.5) and (imc <= 24.9): return "Saudavel"

     elif (imc >= 25) and (imc <= 29.9): return "Sobrepeso"

     elif (imc > 30) and (imc <= 34.9): return "Obesidade grau 1"

     elif (imc > 35) and (imc <= 39.9): return "Obesidade severa grau 2"

     else : return "Obesidade morbida grau 3"

peso

altura

resultado = calculadoraImc(peso,altura)

print(resultado)