import sys
import json

# 1 :Ajouter un élément à la liste de courses
# 2 :Retirer un élément de la liste de courses
# 3 :Afficher les éléments de la liste de courses
# 4 :Vider la liste de courses
# 5 :Quitter le programme

#Création d'une liste vide
sauvegarde = "/Users/victor/Info/Python_Udemy/Partie_2/S35_Liste_de_course_avec_sauvegarde/Sauvegarde.json"
with open(sauvegarde, "r") as f:
    liste = json.load(f)

#Garder le programme actif dans que l'option 5 n'a pas été choisi
while True :
    #Selection d'un choix
    choix = input ("""
    1 :Ajouter un élément à la liste de courses
    2 :Retirer un élément de la liste de courses
    3 :Afficher les éléments de la liste de courses
    4 :Vider la liste de courses
    5 :Quitter le programme)
    ---------> Votre choix : """)

    #Ajouter un objet à la liste
    if choix == "1":
        objet = input("Que souhaitez vous ajouter à la liste? ")   #On demande l'objet à insérer
        liste.append(objet)
    
    #Retirer un objet de la liste
    elif choix == "2":
        sup = input("Entrer l'élément à retirer de votre liste: ")
        if sup in liste:
            liste.remove(sup)
            print(f"L'élément {sup} a bien été supprimé de votre liste")
        else : 
            print(f"{sup} ne fait pas partie de votre liste")
    #Afficher la liste avec leur indice
    elif choix == "3":
        if liste == []:
            print("Votre liste est vide")
        for i, contenu in enumerate(liste):
            print(f"{i+1}. {contenu}")

    elif choix == "4":
        liste.clear()
    elif choix == "5":
        print("A bientôt")
        with open(sauvegarde, "w") as f:
            json.dump(liste, f, indent = 2)
        sys.exit()
    else:
        continue
    