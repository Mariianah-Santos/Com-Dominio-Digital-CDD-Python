# while True:
#     try:
#         num1 = int(input("NUMERO 1º => "))
#         num2 = int(input("NUMERO 2º => "))   
#     except:
#         print("DIGITE APENAS NUMEROS")
#     else:
#         try:
#             div = num1 / num2
#         except ZeroDivisionError:
#             print("O numero não é divisivel por 0")
#         else:
#             print(div)
#             break

cont = False
while not cont:
    try:
        num1 = int(input("NUMERO 1º => "))
        num2 = int(input("NUMERO 2º => "))
        div = num1 / num2
        print(f"A DIVISÃO É => ({div})")   
        cont = True
    except ZeroDivisionError:
        print("O numero não é divisivel por 0")
    except ValueError:
        print("DIGITE SO NUMEROS POR FAVOR!!")