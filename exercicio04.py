"""Faça um código que receba o número de alunos de uma sala de aula e depois solicite as notas
desses alunos, no final, mostre a média aritmética da turma."""

numAluno = int(input("Digite a quantidade de alunos: "))
i = 0
soma = 0

while i < numAluno:
    valor = float(input("Digite a nota: "))
    soma += valor
    i += 1
media = soma/numAluno
print(f"Sua média é: {media}")