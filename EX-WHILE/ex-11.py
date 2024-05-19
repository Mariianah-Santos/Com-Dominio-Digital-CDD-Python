# 6. Ler um valor e escrever a mensagem É MAIOR
# QUE 10! se o valor lido for maior que 10, caso
# contrário escrever NÃO É MAIOR QUE 10!

resp = "S"
while resp == "S" or resp == "s":
    numero = int(input("NUMERO => "))
    if numero > 10:
        print(f"ESSE NUMERO [{numero}] É MAIOR QUE [10]")
    else:
        print(f"ESSE NUMERO [{numero}] É MENOR QUE [10]")
    resp = input("TENTAR COM OUTRO NUMERO? [S/N] ")
print("-/-"*5)
print("SAINDO...")