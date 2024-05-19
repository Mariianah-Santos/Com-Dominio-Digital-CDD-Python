# Desafio: Altere o código anterior e acrescente a
# opção de aluno em recuperação, caso sua média
# seja menor que 7,0 e maior que 4,00

nota_1 = float(input("NOTA 1: "))
nota_2 = float(input("NOTA 2: "))
nota_3 = float(input("NOTA 3: "))
media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print("APROVADO", media)
elif media < 7 and media >= 4:
    print("RECUPERAÇÃO", media)
else:
    print("REPROVADO", media)