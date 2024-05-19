# Faça um código para ler a senha de
# um usuário e após 3 tentativas
# erradas, sair do programa,
# informando que a senha está
# bloqueada

senha = "Mariana"
senhaSecreta = input("SENHA: ")
cont = 1
while cont < 3:
    if senha != senhaSecreta:
        senhaSecreta = input(f"SENHA {cont}º TENTATIVA: ")
        cont += 1
    else:
        print("SEJA BEM-VINDO DE VOLTA!!")
        break
    if cont == 3:
        print("CONTA BLOQUEADA!!")
        break