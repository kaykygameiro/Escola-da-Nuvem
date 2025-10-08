# classifica_numeros.py
# Classifica números como pares ou ímpares e conta quantos de cada tipo foram digitados

print("=== Classificador de Números ===")
pares = 0
impares = 0

while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    if num % 2 == 0:
        pares += 1
        print(f"{num} é par.")
    else:
        impares += 1
        print(f"{num} é ímpar.")

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
