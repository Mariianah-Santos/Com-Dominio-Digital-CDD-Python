## exercicio 1

# Faça um programa para imprimir:
# 1
# 2 2
# 3 3 3

def hieraquia(num): ## define o nome da função e o parametro
    for cont in range(1, num+1):
        for cont_1 in range(cont):
            print(cont, end="")
        print()

#############################################

## exercicio 2

# Faça um programa para imprimir:
# 1
# 1 2
# 1 2 3

def hieraquia_equilibrada(num):
    for cont in range(1, num+1):
        for cont_1 in range(cont):
            print(cont_1+1, end=" ")
        print()



