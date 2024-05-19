# 8. Faça um código que receba 4
# números e realize a soma deles e a
# média entre eles. e mostre os
# resultados.

soma = 0
for cont in range(4):
    numero = int(input(f"{cont+1}º NUMERO => "))
    soma = soma + numero
media = soma / 4
print(f"A MEDIA É {media}")