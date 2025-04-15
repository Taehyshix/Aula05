"""Faça um código para ler a senha de um usuario e após 3 tentativas erradas, sair do programa,
informando  que a senha está bloqueada."""
senha = 1234
pedirSenha = int(input("Digite a senha: "))
tentativas = 1

while pedirSenha != senha and tentativas <3:
    pedirSenha = int(input("Tente novamnete: "))
    tentativas = tentativas+1
if pedirSenha == senha:
    print("Usuário conectado!")
else:
    print("Usuário bloqueado!")