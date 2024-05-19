# Ler 10 valores, calcular e
# escrever a média aritmética
# desses valores

cont = 1
soma = 0
while cont < 11:
    num = float(input(f"NUMERO {cont} => "))
    soma = soma + num
    cont += 1
media = soma / 10
print(f"A MEDIA GERAL É {media}")