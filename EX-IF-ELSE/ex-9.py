# 3. Crie um código que leia a idade de
# uma pessoa e diga em qual ano ela
# nasceu

idade = int(input("IDADE: "))
ano_atual = 2024
aniversario = input("JÁ FEZ ANIVESÁRIO ESSE ANO? [S/N] ")
if aniversario == "S" or aniversario == "s":
    nascimento = ano_atual - idade
    print(f"ANO DE NASCIMENTO É {nascimento}")
else:
    nascimento = ano_atual - idade - 1
    print(f"ANO DE NASCIMENTO É {nascimento}")