#Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.
#(usando While)
i = 0
soma = 0

while i < 10:
    valor = float(input("Digite um valor: "))
    soma += valor
    i += 1
media = soma/10
print(f"Sua média é: {media}")