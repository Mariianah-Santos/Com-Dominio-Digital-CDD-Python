# 12. Escreva um algoritmo para ler o
# número total de eleitores de um
# município, o número de votos brancos,
# nulos e válidos. Calcular e escrever o
# percentual que cada um representa em
# relação ao total de eleitores.
voto_nulos = 0
voto_branco = 0
voto_valido = 0
eleitores = int(input("QUANTOS ELEITORES TEM NO MUNICIPIO? "))
for cont in range(eleitores):
    votos = int(input(f"[{cont+1}]º SEU VOTO É? 1 - [NULO] 2 - [BRANCO] 3 - [VÁLIDO]"))
    if votos == 1:
        voto_nulos = voto_nulos + 1
    elif votos == 2:
        voto_branco = voto_branco + 1
    elif votos == 3:
        voto_valido = voto_valido + 1
voto_nulos = voto_nulos / 100
voto_branco = voto_branco / 100
voto_valido = voto_valido / 100
print(f"VOTOS NULOS [{voto_nulos}%]")
print(f"VOTOS EM BRANCO [{voto_branco}%]")
print(f"VOTOS VÁLIDOS [{voto_valido}%]")