# 4. Crie um algoritmo que receba 3
# números e informe qual o maior entre
# eles.

maior = 0
for cont in range(3):
    numero = int(input(f"{cont+1}º NUMERO: "))
    if numero > maior:
        maior = numero
print(f"O MAIOR NUMERO É: {maior}")