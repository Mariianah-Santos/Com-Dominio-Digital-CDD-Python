# Modifique o exercício anterior para aceitar somente valores
# maiores que 0 para N. Caso o valor
# informado (para N) não seja maior que 0, deverá ser lido um
# novo valor para N.
num = int(input("DIGITE UM NUMERO => "))
if num > 0:
    for cont in range(1, num, 1):
        print(cont, end=" ")
else:
    num = int(input("DIGITE UM NUMERO => "))
