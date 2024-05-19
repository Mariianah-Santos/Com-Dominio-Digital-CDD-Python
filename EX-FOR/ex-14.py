# 1. Faça um algoritmo que receba 2 notas e calcule a média aritmética. Se a nota for
# maior que 10 e menor que 0 faça o programa perguntar de novo. 

soma = 0
for cont in range(2):
    nota = float(input(f"DIGITE A {cont+1}º DO ALUNO=> "))
    while nota <0 or nota > 10:
        nota = float(input(f"DIGITE A {cont+1}º DO ALUNO NOVAMENTE=> "))
    soma = soma + nota
media = soma / 2
print(f"A MÉDIA DO ALUNO É: {media}")