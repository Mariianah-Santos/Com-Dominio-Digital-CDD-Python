# Faça um código para ler 2 valores e
# realize a divisão do primeiro pelo
# segundo valor recebido, caso o
# segundo valor digitado, seja zero ,
# solicite novamente o valor, informando
# que só aceitaremos valores diferentes
# de zero.

cont = 1

num_1 = int(input("DIGITE O PRIMEIRO VALOR => "))
num_2 = int(input("DIGITE O SEGUNDO VALOR => "))

if num_2 == 0:
    while cont > num_2:
        num_2 = int(input("DIGITE NOVAMENTE O SEGUNDO VALOR => "))

divisao = num_1 / num_2
print(divisao)