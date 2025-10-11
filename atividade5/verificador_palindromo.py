palavra = input("Digite uma palavra: ")

# Inverte a palavra
palavra_invertida = palavra.reversed()

# Compara as duas palavras
if palavra == palavra_invertida:
    print("Sim")
else:
    print("Não")

