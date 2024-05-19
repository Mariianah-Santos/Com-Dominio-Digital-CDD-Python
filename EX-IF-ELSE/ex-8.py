# receba, do usuário, um número de 1 a 12 e mostre o
# nome do mês correspondente. Caso o mês não
# existir, mostrar essa informação.

num = int(input("DIGITE UM NUMERO PARA SABER O MÊS CORRESPONDENTE => "))
if num < 1 or num > 12:
    print("POR FAVOR DIGITE UM NMERO VÁLIDO [1 A 12]")
elif num == 1:
    print("JANEIRO")
elif num == 2:
    print("FEVEREIRO")
elif num == 3:
    print("MARÇO")
elif num == 4:
    print("ABRIL")
elif num == 5:
    print("MAIO")
elif num == 6:
    print("JUNHO")
elif num == 7:
    print("JULHO")
elif num == 8:
    print("AGOSTO")
elif num == 9:
    print("SETEMBRO")
elif num == 10:
    print("OUTUBRO")
elif num == 11:
    print("NOVEMBRO")
elif num == 12:
    print("DEZEMBRO")
