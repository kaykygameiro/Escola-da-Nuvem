# conversor_moeda.py

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("Valor em reais: R$", valor_reais)
print("Em dólares: US$", round(valor_dolar, 2))
print("Em euros: €", round(valor_euro, 2))
