# 17.As maçãs custam R$ 1,30 cada se forem
# compradas menos de uma dúzia, e R$ 1,00
# se forem
# compradas pelo menos 12. Escreva um
# programa que leia o número de maçãs
# compradas, calcule e
# escreva o custo total da compra.

macas = float(input("QUANTAS MAÇAS VOCÊ COMPROU? R$"))
maca_mais_12 = 1.00
if macas >= 12:
    maca_mais_12 = macas * 1.00
    print(f"O VALOR A PAGAR PELAS [{macas}] É R${maca_mais_12}")
else:
    valor_maca = macas * 1.30
    print(f"O VALOR A PAGAR PELAS [{macas}] É R${valor_maca}")