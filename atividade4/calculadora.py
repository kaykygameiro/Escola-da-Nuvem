# calculadora.py
# Calculadora simples com as 4 operações básicas

print("=== Calculadora Simples ===")
num1 = float(input("Digite o primeiro número: "))
operador = input("Escolha a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero."
else:
    resultado = "Operador inválido!"

print("Resultado:", resultado)
