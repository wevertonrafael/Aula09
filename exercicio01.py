nomes = []
for x in range(5):
    nome = input("Digite o nome: ")
    nomes.append(nome)
nomes_com_a = [nome for nome in nomes if 'a' in nome.lower()]
print("Nomes que contêm a letra 'A':")
for nome in nomes_com_a:
    print(nome)
