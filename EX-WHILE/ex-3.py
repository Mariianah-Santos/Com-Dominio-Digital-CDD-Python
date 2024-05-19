# Faça um código que receba o
# número de alunos de uma sala de
# aula e depois solicite as notas
# desses alunos, no final, mostre a
# média aritmética da turma.
qtd_alunos = int(input("NUMEROS DE ALUNOS => "))
cont = 1
soma = 0
while cont < qtd_alunos:
    notas = float(input(f"{cont}º NOTA: "))
    soma += notas
    cont += 1
media = soma / qtd_alunos
print(f"A MEDIA É {media}")