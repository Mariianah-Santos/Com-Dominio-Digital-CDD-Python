# Ler 10 valores e escrever quantos desses valores lidos
# são NEGATIVOS.

negativo = 0
for cont in range(1, 11, 1):
    num = int(input(F"DIGITE O {cont}º NUMERO => "))
    if num < 0:
        negativo = negativo + 1
print(f"TEM {negativo} NUMEROS NEGATIVOS")