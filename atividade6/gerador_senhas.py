import random
import string

tamanho = int(input("Digite o tamanho da senha: "))

caracteres = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print(f"Senha gerada: {senha}")