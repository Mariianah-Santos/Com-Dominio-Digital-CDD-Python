# 6. Ler um valor e escrever a mensagem É MAIOR
# QUE 10! se o valor lido for maior que 10, caso
# contrário escrever NÃO É MAIOR QUE 10!

numero = int(input("NUMERO => "))
if numero > 10:
    print(f"ESSE NUMERO [{numero}] É MAIOR QUE [10]")
else:
    print(f"ESSE NUMERO [{numero}] É MENOR QUE [10]")