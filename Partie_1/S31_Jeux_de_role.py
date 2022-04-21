from random import randint
import sys


#Le but de ce projet est de créer un jeu de rôle textuel dans le terminal.
#Le jeu comporte deux joueurs : vous et un ennemi.
#Vous commencez tous les deux avec 50 points de vie.
#Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.
#L'ennemi ne dispose d'aucune potion.
#Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.
#Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.
#L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.
#Lorsque vous utilisez une potion, vous passez le prochain tour.

joueur = 50
ordi = 50
potion = 3
ato = randint(5,15)
tour_passe = False


while True:
    if tour_passe == True:
        print("Vous passez votre tour")
        tour_passe = False
    else:
    
        action = input("Souhaitez vous attaquer (1) ou prendre une potion (2)? \n" )

        while action == "2" and potion == 0 :
            print("Vous n'avez plus de potion!")
            action = input("Souhaitez vous attaquer (1) ou prendre une potion (2)? ")
            print("")
    
    
        if action == "1":
            atj = randint(5,10)
            ordi -= atj
            print(f"Vous avez infligé {atj} à l'ennemi")
        elif action == "2" and potion !=0:
            recup_vie = randint(15,50)
            joueur += recup_vie
            potion -= 1
            print(f"Vous récupérez {recup_vie} points de vie.")
            tour_passe = True


    if (action == "1" or action == "2") and (joueur > 0 and ordi > 0):
        ato = randint(5,15)
        joueur -= ato
        print(f"L'ennemi vous a infligé {ato} point de dégats")
        print("")
        print(f"Il vous reste {joueur} points de vie")
        print(f"Il reste {ordi} point de vie à l'ennemi")
        print(50 * "*")
        


    if ordi <= 0 :
        print("Tu as gagné!!")
        sys.exit()
    elif joueur <= 0:
        print("Dommage tu as perdu... Retente ta chance!")
        sys.exit()





