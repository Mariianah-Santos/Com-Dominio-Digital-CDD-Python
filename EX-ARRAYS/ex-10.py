# Altere o sistema anterior e faça um sistema
# de login, pedindo a senha do usuário e
# mostrando seu nome e a mensagem, login
# efetuado com sucesso.

nomes = ["", "", "", "", ""]
senhas = ["", "", "", "", ""]
index = 0
cont = True
usuario_encontrado = False
while cont:
    print("MENU \n[1] - CADASTRE-SE \n[2] - LOGIN")
    opcao = int(input("OPÇÃO ESCOLHIDA => "))
    if opcao == 1:
        for cadastro in range(len(nomes)):
            nomes[cadastro] = input("NOME PARA CADASTRO: ")
            senhas[cadastro] = input("SENHA PARA CADSTRO: ")
            print("CADASTRO REALIZADO COM SUCESSO!!")
            print()
    if opcao == 2:
        nome_usuario = input("USUÁRIO: ")
        senha_usuario = input("SENHA: ")
        for nome in nomes:
            if nome != "":
                if nome == nome_usuario and senhas[index] == senha_usuario:
                    print("USUARIO ENCONTRADO")
                    cont = False
                    usuario_encontrado = True
                    break
            index +=1 
        if not usuario_encontrado:
            print("USÚARIO NÃO ENCONTRADO OU SENHA INCORRETA!")




            # if nomes[login] == nome and senhas[login] == senha:
            #     print("ENTRANDO...")
            #     cont = False
            # else:
            #     print("USUÁRIO NÃO ENCONTRADO OU SENHA INCORRETA!!")
            #     print()
