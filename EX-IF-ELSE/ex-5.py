# Escreva um algoritmo que leia o número de litros
# vendidos e o tipo de combustível (codificado da
# seguinte forma: E-etanol, G-gasolina), calcule e
# imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina é R$
# 5,80 e o preço do litro do etanol é R$ 4,90.

litros = int(input("LITROS: "))
tipo_combust = input("E-ETANO R$4,90 | G-GASOLINAA R$5,80 => ")
etanol = 4.90
gasolina = 5.80
if tipo_combust == "E" or tipo_combust == "e":
    valor_pagar = litros * etanol
    print(f"COMPROU ETANOL VALOR A PAGAR R${valor_pagar}")
elif tipo_combust == "G" or tipo_combust == "g":
    valor_pagar = litros * gasolina
    print(f"COMPROU GASOLINA VALOR A PAGAR R${valor_pagar}")
else:
    print("INVÁLIDO!! POR FAVOR DIGITE UMA LETRA VÁLIDA!! [E/G]")