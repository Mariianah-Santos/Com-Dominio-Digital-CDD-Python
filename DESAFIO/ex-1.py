notas = []

for cont in range(4):
    nota = float(input(f"{cont+1}º NOTA: "))
    notas.append(nota)

print(notas)
soma = notas[0] + notas[1] + notas[2] + notas[3]
media = soma / 4

if media >= 7:
    print(f"APROVADO COM MÉDIA {media}")
elif media >= 5:
    print(f"RECUPERAÇÃO COM MÉDIA {media}")
else: 
    print(f"REPROVADO COM MÉDIA {media}")