import random


def jogar():
    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Defina o nivel: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(chute_maior):
                print("Voce errou! O seu chute foi maior que o numero secreto!")
            elif(chute_menor):
                print("Voce errou! O seu chute foi menor que o numero secreto!")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("fim do jogo")


if(__name__ == "__main__"):
    jogar()
