def jogar():
    print("**************")
    print("Jogo da forca!")
    print("**************")

    palavra_secreta, enforcado, acertou, chance = criaJogo()
    palavra_desenhada = desenhaPalavra(palavra_secreta)
    print(palavra_desenhada)


    while (not enforcado and not acertou):
        chute = input("Chute uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Você acertou uma letra!")
                palavra_desenhada[index] = letra
                print(palavra_desenhada)
            index += 1

        fim = "_" not in palavra_desenhada
        chance -= 1
        print("Você tem {} chances".format(chance))
        if (fim):
            print("Você venceu!")
            break
        elif (chance == 0): 
            print("Perdeu!")
            break

        


#def fimJogo():


def criaJogo():
    palavra_secreta = input("Digite a palvra secreta: ").upper()
    enforcado = False
    acertou = False
    chance = 10
    return palavra_secreta, enforcado, acertou, chance


def desenhaPalavra(palavra_correta):
    lista = []
    for letras in palavra_correta:
        lista.append("_")
    return lista




if (__name__ == "__main__"):
    jogar()
