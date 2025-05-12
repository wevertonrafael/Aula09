
numero_secreto = 50
tentativas_restantes = 5

print("Adivinhe o número secreto!")
print("Você tem 5 tentativas.")

while tentativas_restantes > 0:
    chute = int(input(f"Digite seu palpite ({tentativas_restantes} tentativa(s) restantes): "))

    if chute == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    elif chute < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")

    tentativas_restantes -= 1

if tentativas_restantes == 0:
    print(f"Fim de jogo! O número secreto era {numero_secreto}.")
