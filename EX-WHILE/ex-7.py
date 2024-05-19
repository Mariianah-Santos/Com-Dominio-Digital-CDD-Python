# Refaça o exercício anterior, agora
# implementando a pergunta:
# “Deseja realizar novo cálculo?”

resp = "S"
while resp == "S" or resp == "s":
    nota_1 = float(input("NOTA 1º => "))
    while nota_1 <= 0 or nota_1 > 10:
        nota_1 = float(input("DIGITE NOVAMENTE A 1º NOTA => "))
    nota_2 = float(input("NOTA 2º => "))
    while nota_2 <= 0 or nota_2 > 10:
        nota_2 = float(input("DIGITE NOVAMENTE A 2º NOTA => "))
    media = (nota_1 + nota_2) / 2
    print(media)
    resp = input("DESEJA FAZER UM NOVO CALCULO? [S/N]")
print("FINALIZANDO O PROGRAMA...")