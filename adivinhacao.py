import random

def jogar():

    print("*******************************")
    print("bem vindo ao jogo de advinhação")
    print("*******************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 100

    print("Escolha o nivel de dificuldade")
    print("1 -facil, 2 - medio, 3 -dificil")
    nivel = int(input("digite o nivel \n" ))

    if(nivel==1):
            total_de_tentativas = 20
    elif(nivel==2):
            total_de_tentativas = 10
    else:
            total_de_tentativas = 5


    for rodada in range ( 1, total_de_tentativas+1):
        chute = input("Digite o seu numero entre 1 e 100 \n")
        numero = int(chute)
        print("voce digitou... ", chute, end="\n")
        print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
        if(numero <1 or numero >100):
            print("Voce deve digitar um numero entre 1 e 100 \n")

            continue

        acertou = numero == numero_secreto
        maior = numero > numero_secreto
        menor = numero < numero_secreto


        if (acertou):
            print("voce acertou!!! \n")
            break
        else:
            if(maior):
                print("voce errouuuuu o seu chute foi maior que o numero escolhido \n")
            elif(menor):
                print( "o seu chute foi menor que o numero escolhido \n")

            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos


    print("fim de jogo o numero secreto era...", numero_secreto )
    print("E voce fez {} pontos".format(pontos))


if(__name__ =="__main__"):
    jogar()
