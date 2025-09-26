# calculadora_desconto.py

produto = "Camiseta"
preco_original = 50.00
desconto = 20  # em %

valor_desconto = preco_original * (desconto / 100)
preco_final = preco_original - valor_desconto

print("Produto:", produto)
print("Preço original: R$", preco_original)
print("Desconto:", desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))
