# 11. Faça um algoritmo que leia a idade de
# uma pessoa expressa em anos, meses e dias
# e escreva a idade dessa pessoa expressa
# apenas em dias. Considerar ano com 365
# dias e mês com 30 dias.

ano_atual = 2024
ano_nascimento = int(input("ANO DE NASCIMENTO: "))
mes = int(input("MÊS DE NASCIMENTO: "))
dia_nascimento = int(input("DIA DE NASCIMENTO: "))
idade = ano_atual - ano_nascimento
dias_na_terra = (dia_nascimento + (idade * 365) + (mes * 30))
print(f"DATA: {dia_nascimento}/{mes}/{ano_nascimento}")
print(f"DIAS NA TERRA {dias_na_terra}\nIDADE ATUAL: {idade}")
