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


"""Resolução do prof: 
pin = 1234
tentativas = 1
mensagem="Acesso Bloqueado!"

while tentativas<=3:
    senha=int(input("Digite a senha"))
    if senha == pin:
        mensagem="Login efetuado com sucesso!"
        break 
    tentativas = tentativas + 1
print(mensagem)"""