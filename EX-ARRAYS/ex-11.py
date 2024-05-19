# Altere o sistema anterior e faça um sistema
# de login, pedindo a senha do usuário e
# mostrando seu nome e a mensagem, login
# efetuado com sucesso.

nomes = ["", "", "", "", ""]
senhas = ["", "", "", "", ""]
while True:
    print("MENU \n[1] - CADASTRE-SE \n[2] - LOGIN")
    opcao = int(input("OPÇÃO ESCOLHIDA => "))
    if opcao == 1:
        for cadastro in range(len(nomes)):
            nomes[cadastro] = input("NOME PARA CADASTRO: ")
            senhas[cadastro] = input("SENHA PARA CADSTRO: ")
            print("CADASTRO REALIZADO COM SUCESSO!!")
            print()
    elif opcao == 2:
        nome = input("USUÁRIO: ")
        senha = input("SENHA: ")
        for login in range(len(nomes)):
            if nome == nomes[login] and senha == senhas[login]:
                print("ENTRANDO...")
                break
        else:
            print("USUÁRIO NÃO ENCONTRADO OU SENHA INCORRETA!!")
    else:
        print("FINALIZANDO O PROGRAMA...")
        break
print("FIM...")
