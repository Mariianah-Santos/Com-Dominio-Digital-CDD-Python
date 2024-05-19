# 2. Crie um código que leia um número
# diferente de zero e diga se este número
# é positivo ou negativo e pergunte se ele quer fazer com outro numero

resp = "S"
while resp == "S" or resp == "s":
    numero = int(input("NUMERO: "))
    if numero > 0:
        print(f"O NÚMERO {numero} É POSITIVO")
    else:
        print(f"O NÚMERO {numero} É NEGATIVO")
    resp = input("QUER TENTAR COM OUTRO NUMERO? [S/N]: ")
print("SAINDO...")