from curses.ascii import isdigit
from random import randint
import sys
from unicodedata import digit
###Jeux du nombre Mystère###
nb_myst = randint(0,10)
vie = 5

print("*** Le jeux du nombre mystère ***")
while vie != -1 : #boucle tant que on a encore des tentative
    if vie == 0: #Si plus de vie (=0) le jeux s'arrête
       print(f"Dommage tu as perdu. Le nombre mystère était {nb_myst}")
            

    print(f"Il te reste {vie} essaies")
    nb = input("Devine le nombre : ")

    if not nb.isdigit(): #Verification que le joueur rentre bien un nombre
        print("Veuillez entrer un nombre valide")
    
    elif int(nb) > nb_myst: #si le nombre donné est supérier au nombre mystère
        print(f"Le nombre mystère est inférieur à {nb}")
        vie -= 1
    elif int(nb) < nb_myst: #Si le nombre donné est inférieur au nombre mystère
        print(f"Le nombre mystère est supérieur à {nb}")
        vie -= 1
    elif int(nb) == nb_myst: #Si le nombre donné est le nombre mystère
        print(f"Bravo! Le nombre était bien {nb_myst}.\n Tu as trouvé en {6-vie} essaies. \n Fin du jeux.")
        sys.exit()


  
    
        
