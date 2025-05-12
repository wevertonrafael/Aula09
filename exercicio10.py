frase = input("Digite uma frase: ")
cont=0
for x in range(len(frase)):
    if frase[x] == "a":
      cont+=1
print(cont)