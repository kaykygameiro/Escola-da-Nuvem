# verifica_senha.py
# Verifica se a senha atende critérios básicos de segurança

print("=== Verificador de Senha ===")
senha = input("Digite uma senha: ")

tem_numero = any(char.isdigit() for char in senha)
tamanho_ok = len(senha) >= 8

if tamanho_ok and tem_numero:
    print("Senha válida!")
else:
    print("Senha inválida! Deve ter pelo menos 8 caracteres e conter números.")
