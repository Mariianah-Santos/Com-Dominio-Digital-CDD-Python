# Ler um vetor A de 10 números. logo em
# seguida, ler mais um número e guardar em
# uma variável X.
# Armazenar em um vetor M o resultado de
# cada elemento de A multiplicado pelo
# valor X. Logo após, imprimir o vetor M.

# A = [0,0,0,0,0,0,0,0,0,0]
# M = [0,0,0,0,0,0,0,0,0,0]

# for cont in range(len(A)):
#     A[cont] = int(input(f"DIGITE O {cont+1}º NUMERO => "))
# x = int(input("DIGITE O NUMERO QUE IRÁ SER O MULTIPLICADOR => "))
# for cont_m in range(len(A)):
#     M[cont_m] = x * A[cont_m]
# print(x, "X", A, "=", M)

A = [0,0,0,0,0,0,0,0,0,0]
M = [0,0,0,0,0,0,0,0,0,0]
x = int(input("DIGITE O NUMERO QUE IRÁ SER O MULTIPLICADOR => "))
for cont in range(len(A)):
    A[cont] = int(input(f"DIGITE O {cont+1}º NUMERO => "))
for new_tab in range(len(A)):
    for cont_m in range(len(A)):
        M[cont_m] = x * A[cont_m]
    print(x, "X", A[new_tab], "=", M[new_tab])
