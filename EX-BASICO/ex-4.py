# 4. Crie um algoritmo que receba 3 números e informe qual o maior entre eles.

num_1 = int(input("NUMERO 1 => "))
num_2 = int(input("NUMERO 2 => "))
num_3 = int(input("NUMERO 3 => "))

if num_1 > num_2 and num_1 > num_3:
    print("O NUMERO 1 É O MAIOR",num_1)
elif num_2 > num_1 and num_2 > num_3:
    print("O NUMERO 2 É O MAIOR", num_2)
else:
    print("O NUMERO 3 É O MAIOR", num_3)