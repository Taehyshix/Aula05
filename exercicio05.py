"""Faça um código para ler 2 valores e realize a divisão do primeiro pelo segundo valor recebido, caso o
segundo valor digitado, seja zero , solicite novamente o valor, informando que só aceitaremos diferente de zero."""

valor1 = float(input("Digite o primiero valor: "))
valor2 = float(input("Digite o segundo valor: "))

while valor2 == 0:
    valor2 = float(input("Digite o valor diferente de zero: "))

divisao = valor1/valor2
print ("O resultado é: ", divisao)
#while é um if que repete, fazendo um loop