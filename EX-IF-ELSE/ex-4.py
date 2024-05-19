# Ler o nome de 2 times e o número de gols
# marcados na partida (para cada time).
# Escrever o nome do vencedor. Caso não
# haja vencedor deverá ser impressa a
# palavra EMPATE.

time1 = input("NOME DO PRIMEIRO TIME: ")
gol_time1 = int(input("PRIMERIO TIME: GOLS MARCADO NA PARTIDA => "))
time2 = input("NOME DO SEGUNDO TIME: ")
gol_time2 = int(input("SEGUNDO TIME: GOLS MARCADO NA PARTIDA => "))

if gol_time1 > gol_time2:
    print(f"VENCEDOR FOI {time1} COM {gol_time1} GOLS")
elif gol_time1 == gol_time2:
    print(f"EMPATE AMBOS OS TIMES [{gol_time1}] X [{gol_time2}] DE GOLS")
else:
    print(f"VENCEDOR FOI {time2} COM {gol_time2} GOLS")