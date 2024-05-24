# num1 = int(input("NUMERO 1º: "))
# num2 = int(input("NUMERO 2º: "))

# try:
#     div = num1 / num2
#     if num1 == 0 or num2 == 0:
#         print(div)
#     else:
#         print(div)
# except:
#     print("o numero não pode ser divisivel por zero!!")


num1 = int(input("NUMERO 1º: "))
num2 = int(input("NUMERO 2º: "))

try:
    div = num1 / num2 or num2 / num1
except ZeroDivisionError:
    print("o numero não pode ser divisivel por zero!!")
else:
    print(f"A divisão dos numeros é {div}")