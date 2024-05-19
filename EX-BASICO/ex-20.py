# 15. Escreva um algoritmo para ler dois
# valores (considere que não serão lidos
# valores iguais) e escrevê-los em ordem
# crescente

num_1 = int(input("PRIMEIRO NUMERO => "))
num_2 = int(input("SEGUNDO NUMERO => "))
if num_1 > num_2:
    print(f"{num_2} - {num_1}")
else:
    print(f"{num_1} - {num_2}")