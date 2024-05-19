# Escreva um código que permita a leitura
# das notas de uma turma de 5 alunos e
# guarde num vetor, Calcular a média da
# turma e contar quantos alunos obtiveram
# nota acima desta média calculada
# Escrever a média da turma e o resultado
# da contagem

notas = [0,0,0,0,0]
soma = 0
notas_maior_media  = 0
for cont in range(len(notas)):
    notas[cont] = float(input(f"QUAL A NOTA DO {cont+1}º ALUNO => "))
for cont_soma in range(len(notas)):
    soma = soma + notas[cont_soma]
media = soma / len(notas)
for cont_media in range(len(notas)):
    if notas[cont_media] >= media:
        notas_maior_media = notas_maior_media  + 1
print(f"A MÉDIA DOS ALUNOS É {media} \nA QUANTIDADE DE ALUNOS QUE TIRARAM NOTA MAIOR OU IGUAL A MÉDIA É {notas_maior_media}")