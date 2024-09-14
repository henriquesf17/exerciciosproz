# 1 Escreva um código que imprima todos os números exceto o número 13.
# 2 Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.
# 3 Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

#1 - For
print("For")

for n in range(1,21):
    if n == 13:
        continue
    print(n)

#2 - While
print("While")

i = 1
while i <= 20:
    if i == 13:
        i += 1
        continue
    print(i)
    i += 1

# 3 - Regresso
print("While regresso")

i = 20
while i >= 1:
    if i == 13:
        i -= 1
        continue
    print(i)
    i -= 1