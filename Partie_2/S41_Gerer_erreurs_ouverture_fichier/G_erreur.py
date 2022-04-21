from pathlib import Path


#Gestion d'erreur lorsque l'utilisateur rentre un fichier inexistant ou illisible.

lecture = Path.home() /input("Entrer le nom du fichier avec son extension : ")


try:
    f = open(lecture, "r")
    print(f.read())

except UnicodeDecodeError:
    print("Le fichier est illisible")

except FileNotFoundError:
    print("Le fichier n'a pas été trouvé")

else:
    f.close()
   


   