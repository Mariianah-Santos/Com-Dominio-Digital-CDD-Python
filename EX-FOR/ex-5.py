# Receber 10 números do usuário e mostre a
# soma de todos os números ímpares.
soma = 0
for cont in range(1, 11, 1):
    num = int(input(f"DIGITE O {cont}º NUMERO => "))
    if num % 2 == 1:
        soma = soma + num
print("A SOMA DOS NUMEROS IMPARES É:", soma)