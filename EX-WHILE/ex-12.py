# 7. Faça um código que receba o valor da
# base e da altura de um triângulo e
# calcule sua área. usando a fórmula A =
# (base x Altura ) /2

resp = "S"
while resp == "S" or resp == "s":
    base = int(input("BASE: "))
    altura = int(input("ALTURA: "))
    area = (base * altura) /2
    print(f"A ÁREA DE UM TRIANGULO É {area}")
    resp = input("TENTAR DENOVO? [S/N] ")
print("SAINDO...")