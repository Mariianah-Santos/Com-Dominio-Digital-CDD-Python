# faça uma função que conte quantas
# vogais tem num texto.
# texto
# O rato roeu a roupa do rei de Roma

# texto = input("DIGITE: ")
# print(len(texto))

# texto = input("DIGITE: ")
# for cont in range(len(texto)):
#     print(cont+1)

espaco_vazio = 0
texto = input("DIGITE: ")
for cont in range(len(texto)):
    if texto == "a" or cont == "e" or cont == "i" or cont == "o" or cont == "u":
        espaco_vazio += 1

print(espaco_vazio)