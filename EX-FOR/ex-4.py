# receber um número do usuário e mostrar todos os
# números ímpares do intervalo de 1 até o número
# digitado

num = int(input("DIGITE UM NUEMRO => "))
for cont in range(1, num, 1):
    if cont % 2 == 1:
        print("[", cont, "]", end=" ")