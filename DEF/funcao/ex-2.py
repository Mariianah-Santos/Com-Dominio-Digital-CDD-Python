# Faça um programa para imprimir:
# 1
# 1 2
# 1 2 3


# num = int(input("NUMERO: "))
# for cont in range(1, num+1):
#     for cont_1 in range(cont):
#         print(cont_1+1, end=" ")
#     print()

# def hieraquia_equilibrada():
#     num = int(input("NUMERO: "))
#     for cont in range(1, num+1):
#         for cont_1 in range(cont):
#             print(cont_1+1, end=" ")
#         print()
# hieraquia_equilibrada()


def hieraquia_equilibrada(num):
    for cont in range(1, num+1):
        for cont_1 in range(cont):
            print(cont_1+1, end=" ")
        print()
hieraquia_equilibrada(3)

# def hieraquia_equilibrada(num):
#     for cont in range(1, num+1):
#         for cont_1 in range(cont):
#             print(cont_1+1, end=" ")
#         print()

# a classe será chamada em outra pasta ;)