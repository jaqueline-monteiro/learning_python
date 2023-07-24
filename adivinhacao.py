print("Bem vindo ao jogo de Adivinhação")

NUMERO_SECRETO = 42

chute = input("Digite o seu número: ")

print("Você digitou: ", chute)

if int(NUMERO_SECRETO) == int(chute):
    print("Você acertou!")
else:
    print("Você errou!")
