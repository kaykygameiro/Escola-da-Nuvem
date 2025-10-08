# media_turma.py
# Registra notas de alunos e calcula a média da turma

print("=== Média da Turma ===")
qtd = int(input("Quantos alunos tem na turma? "))
soma = 0

for i in range(qtd):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma += nota

media = soma / qtd
print(f"A média da turma é: {media:.2f}")
