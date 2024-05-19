# Dados os valores de horários abaixo, decifre a lógica e faça
# um código para executar.
# entrada01 3:45
# entrada02 14:20
# saída 6:05

entrada01hora = int(input("ENTRADA 1 [HORA] => "))
entrada01minutos = int(input("ENTRADA 1 => [MINUTOS] "))

entrada02hora = int(input("ENTRADA 2 [HORA] => "))
entrada02minutos = int(input("ENTRADA 2 => [MINUTOS] "))

soma = (entrada01hora + entrada02hora + entrada01minutos + entrada02minutos)
somaMinutos = (entrada01minutos + entrada02minutos)

if soma > 12:
    entrada01hora = entrada01hora - 12
if soma > 12:
    entrada02hora = entrada02hora - 12
hora = entrada01hora + entrada02hora
if somaMinutos >= 60:
    somaMinutos = somaMinutos - 60
    hora = hora + 1
print(hora,":",somaMinutos)
