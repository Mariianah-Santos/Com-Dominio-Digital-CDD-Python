# Ler uma variável de número inteiro e mostrar a
# tabuada de multiplicação desse número.

num = int(input("NUMERO PARA SABER A TABUADA: "))
for cont in range(1, 11, 1):
    tabuada = num * cont
    print(f"{num} X {cont} = [{tabuada}]")