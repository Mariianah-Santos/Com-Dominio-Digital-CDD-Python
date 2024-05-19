# Modifique o exercício anterior para aceitar somente valores
# maiores que 0 para N. Caso o valor
# informado (para N) não seja maior que 0, deverá ser lido um
# novo valor para N.

numeros = 1
num = int(input("NUMERO => "))
if num > 0:
    while numeros < num:
        print(numeros, end=" ")
        numeros = numeros + 1
else:
    num = int(input("NUMERO => "))