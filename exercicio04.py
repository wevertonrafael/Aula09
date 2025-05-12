soma = 0
for i in range(5):
    number = int(input("Digite um número: "))
    soma = soma + number
media = soma/5
print(media)
if media>= 7:
    print("Aluno Aprovado: ")
elif media <4:
    print("Aluno Reprovado: ")
else:
    print("Aluno em recuperação: ")