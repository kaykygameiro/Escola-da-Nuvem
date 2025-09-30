# calculadora_imc.py

try:
    peso = float(input("Digite seu peso em kg (ex: 70.5): "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    if peso > 0 and altura > 0:
        imc = peso / (altura * altura)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"

        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    else:
        print("Peso e altura devem ser valores positivos.")

except ValueError:
    print("Por favor, digite valores numéricos válidos para peso e altura.")