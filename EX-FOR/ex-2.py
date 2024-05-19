# Escreva um algoritmo para ler 10 números e ao final
# da leitura escrever a soma total dos 10 números
# lidos.
soma = 0
for cont in range(1, 11, 1):
    num = int(input(f"NUMERO {cont}º: "))
    soma = soma + num
print(f"A SOMA DE TODOS OS NUMEROS DIGITADOS {soma}")