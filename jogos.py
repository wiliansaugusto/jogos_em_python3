import adivinhacao
import forca


print("***********************")
print("Que comecem os os jogos")
print("***********************")
print("digite o numero correspondente ao jogo")
print("(1) Forca (2) Advinhacçao numerica")

jogo = int(input("informe o seu jogo \n"))

if(jogo == 1):
    print("Voce escolheu o jogo da forca")
    forca.jogar()
elif(jogo == 2):
    print("voce escolheu o jogo de Advinhaçao nuúmerica")
    adivinhacao.jogar()