# Escreva um código para ler as notas
# da 1a. e 2a. avaliações de um aluno,
# calcule e imprima a média desse
# aluno. Só devem ser aceitos valores
# válidos,durante a leitura ,(0 a 10) para
# cada nota.

nota_1 = float(input("NOTA 1º => "))
while nota_1 <= 0 or nota_1 > 10:
    nota_1 = float(input("DIGITE NOVAMENTE A 1º NOTA => "))
nota_2 = float(input("NOTA 2º => "))
while nota_2 <= 0 or nota_2 > 10:
    nota_2 = float(input("DIGITE NOVAMENTE A 2º NOTA => "))
media = (nota_1 + nota_2) / 2
print(media)