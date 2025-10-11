from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte o texto em data
nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
hoje = datetime.now()

# Calcula a diferença
diferenca = hoje - nascimento

print("Você está vivo há", diferenca, "dias.")

