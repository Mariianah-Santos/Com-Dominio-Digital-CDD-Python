# Ler o número de alunos existentes em uma
# turma e, após isto, ler as notas destes alunos,
# calcular e escrever a média aritmética dessas
# # notas lidas

soma = 0
qtd_alunos = int(input("DIGITE A QUANTIDADE DE ALUNOS NA SALA => "))
for cont in range(1, qtd_alunos, 1):
    nota = float(input(f"{cont}º NOTA: "))
    soma = soma + nota
media = soma / qtd_alunos
print(f"A MEDIA GERAL DA TURMA É: {media}")