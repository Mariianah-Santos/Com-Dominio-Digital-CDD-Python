# Faça um código para ler 5 números e
# armazenar em um vetor. Após a leitura
# total dos 5 números, o código deve
# escrever esses 5 números lidos na ordem
# inversa.

numeros = [0,0,0,0,0]
for cont in range(len(numeros)):
    numeros[cont] = int(input(f"NUMERO {cont+1}º => "))
for inversa in range(4, -1, -1):
    print(numeros[inversa], end=" ")