# Faça um código para ler 5 nomes de
# usuários e suas respectivas senhas, e
# armazenar cada lista em um array
# diferente, após completar a digitação,
# imprimir , nome, senha e posição dos
# dados no array

nomes = ["", "", "", "", ""]
senhas = ["", "", "", "", ""]

for cont in range(5):
    print(f"INFORMAÇÃO DA {cont+1}º PESSOAS")
    nomes[cont] = input(f"NOME DA {cont+1}º PESSOA => ")
    senhas[cont] = input(f"SENHA DA {cont+1}º PESSOA => ")
for posicao in range(5):
    print(posicao+1, "º NOME:", nomes[posicao], f"\n{posicao+1}º SENHA: {senhas[posicao]}")