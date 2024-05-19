# Faça um código que receba as 3 notas de um aluno e
# verifique se ele está aprovado ou reprovado.
# Considere que a média para aprovação é 7,0

nota_1 = float(input("NOTA 1: "))
nota_2 = float(input("NOTA 2: "))
nota_3 = float(input("NOTA 3: "))
media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print("APROVADO", media)
else:
    print("REPROVADO", media)