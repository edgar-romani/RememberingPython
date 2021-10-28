import random

def jogar():
    
    print("*****************")
    print("Jogo de adivinha!")
    print("*****************")

    numero_secreto = random.randrange(1,51)
    pontos = 1000

    print ("Escolha a dificuldade do jogo:")
    print (" (1) Fácil\n (2) Médio\n (3) Difícil")
    nivel=int(input("Defina o nível: "))

    if(nivel == 1):
        tentativas = 10
    elif(nivel == 2):
        tentativas = 5
    elif(nivel == 3):
        tentativas = 3

    while tentativas > 0:
        chute = int(input("Digite o palpite: "))

        if (chute == numero_secreto):
            print("Você acertou!")
            break
        elif(chute > numero_secreto):
            print("Errou! Você chutou pra cima!")
        elif(chute < numero_secreto):
            print("Errou! Você chutou pra baixo!")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        tentativas-= 1

        print("Você ainda tem {} tentativa(s) restante(s).".format (tentativas))

    print("Fim de jogo, você fez {} pontos".format (pontos))


if (__name__ == "__main__"):
    jogar()
    
