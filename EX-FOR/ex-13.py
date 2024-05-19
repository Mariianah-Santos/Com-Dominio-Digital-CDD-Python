# Ler 10 valores e escrever quantos desses valores lidos estão no
# intervalo [10,20] (incluindo os
# valores 10 e 20 no intervalo) e quantos deles estão fora deste
# intervalo.

intervalo10a20 = foraIntervalo = 0
for cont in range(1, 11, 1):
    num = int(input(f"DIGITE O {cont}º NUMERO => "))
    if num >= 10 and num <= 20:
        intervalo10a20 = intervalo10a20 + 1
    else:
        foraIntervalo += 1
print(f"DENTRO DO INTERVALOR {intervalo10a20}")
print(f"FORA DO INTERVALOR {foraIntervalo}")