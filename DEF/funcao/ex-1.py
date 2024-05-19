# Faça um programa para imprimir:
# 1
# 2 2
# 3 3 3

# num = int(input("DIGITE UM NUMERO: "))
#     for cont in range(1, num+1):
#         for cont_1 in range(cont):
#             print(cont, end="")
#         print()

# def hieraquia(): ## define o nome da função e sem parametro
#     num = int(input("DIGITE UM NUMERO: "))
#     for cont in range(1, num+1):
#         for cont_1 in range(cont):
#             print(cont, end="")
#         print()
# hieraquia()

def hieraquiaa(num): ## define o nome da função e o parametro
    for cont in range(1, num+1):
        for cont_1 in range(cont):
            print(cont, end="")
        print()
hieraquiaa(3)