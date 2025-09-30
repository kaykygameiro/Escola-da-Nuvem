# classificador_idade.py

try:
    idade = int(input("Digite a sua idade: "))

    if 0 <= idade <= 12:
        categoria = "Criança"
    elif 13 <= idade <= 17:
        categoria = "Adolescente"
    elif 18 <= idade <= 59:
        categoria = "Adulto"
    elif idade >= 60:
        categoria = "Idoso"
    else:
        categoria = "Idade inválida"

    print(f"Com {idade} anos, você é classificado como: {categoria}")

except ValueError:
    print("Por favor, digite um número inteiro válido para a idade.")