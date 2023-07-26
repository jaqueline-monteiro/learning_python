print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

NUMERO_SECRETO = 42
TOTAL_DE_TENTATIVAS = 3
RODADA = 1

for RODADA in range(1, TOTAL_DE_TENTATIVAS + 1):
    print("Tentativa {} de {}".format(RODADA, TOTAL_DE_TENTATIVAS))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = NUMERO_SECRETO == chute
    maior = chute > NUMERO_SECRETO
    menor = chute < NUMERO_SECRETO

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    print("Fin do jogo!")
