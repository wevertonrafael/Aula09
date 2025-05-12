senha = 1234
codigo = int(input("Digite a senha: "))

while codigo != senha:
    print("Senha incorreta. tente novamente! ")
    codigo = int(input("Digite a senha: "))
print("Acesso liberado! ")
