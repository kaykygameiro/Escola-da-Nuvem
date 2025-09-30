# conversor_temperatura.py

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

try:
    temp = float(input("Digite a temperatura: "))
    unidade_origem = input("Qual a unidade de origem (C, F, K)? ").upper()
    unidade_destino = input("Para qual unidade deseja converter (C, F, K)? ").upper()

    resultado = 0
    if unidade_origem == unidade_destino:
        resultado = temp
    elif unidade_origem == 'C':
        if unidade_destino == 'F':
            resultado = celsius_para_fahrenheit(temp)
        elif unidade_destino == 'K':
            resultado = celsius_para_kelvin(temp)
    elif unidade_origem == 'F':
        if unidade_destino == 'C':
            resultado = fahrenheit_para_celsius(temp)
        elif unidade_destino == 'K':
            resultado = fahrenheit_para_kelvin(temp)
    elif unidade_origem == 'K':
        if unidade_destino == 'C':
            resultado = kelvin_para_celsius(temp)
        elif unidade_destino == 'F':
            resultado = kelvin_para_fahrenheit(temp)
    else:
        print("Unidades inválidas!")
        exit()

    print(f"{temp:.2f}°{unidade_origem} é igual a {resultado:.2f}°{unidade_destino}")

except ValueError:
    print("Por favor, digite um valor numérico para a temperatura.")