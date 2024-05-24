num1 = int(input("NUMERO 1º => "))
num2 = int(input("NUMERO 2º => "))

soma = 0

try:
    if num1 > 200:
        raise OverflowError ## não vai aceitar nada que ultrapasse esse limite que colocamos
    soma = num1 + num2
    print(f"A soma dos numeros é: {soma}")
except OverflowError:
    print("Por favor digite um numero menor que (200)")
