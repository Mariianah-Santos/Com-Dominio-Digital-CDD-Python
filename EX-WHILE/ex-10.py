# 5. Crie um algoritmo que leia um
# número e diga se ele é par ou ímpar

resp = "S"
while resp == "S" or resp == "s":
    numero = int(input("NUMERO: "))
    if numero % 2 == 0:
        print(f"ESSE NUMERO [{numero}] É PAR")
    else:
        print(f"ESSE NUMERO [{numero}] É IMPAR")
    resp = input("QUER TENTAR DE NOVO? [S/N] ")
print("SAINDO...")