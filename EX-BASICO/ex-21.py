# 16. Escreva um algoritmo para ler a hora de
# início e a hora de fim de um jogo de Xadrez
# (considere apenas horas inteiras, sem os
# minutos) e calcule a duração do jogo em
# horas, sabendo-se que o tempo máximo de
# duração do jogo é de 24 horas e que o jogo
# pode iniciar em um dia e terminar no dia
# seguinte

hora_inicio = int(input("HORA DE INICIO: "))
hora_fim = int(input("HORA DO FIM: "))

if hora_inicio < hora_fim:
    hora = hora_fim - hora_inicio
else:
    hora = 24 - hora_inicio + hora_fim
print(f"A HORA DO TÉRMINO {hora}")