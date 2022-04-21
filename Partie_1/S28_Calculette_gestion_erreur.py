#Calculette additionnant 2 nombres avec gestion d'erreur.
#Création de la boucle infini tant que a et b ne sont pas des nombres
while True : 
    #On demande le premier nombre à l'utilisateur qu'on associe à la variable a en s'assurant que a soit comprit comme un entier (int), float si on veut additioner des nombres décimaux.
    a = input("Entrez un premier nombre : ")

    #On demande le deuxième nombre à l'utilisateur qu'on associe à une variable b en s'assurant que b soit comprit comme un entier
    b = input("Entrez un deuxième nombre : ")

    #On effectue l'opération somme
    if a.isdigit() and b.isdigit() :   
        print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a)+int(b)}")
        break
    else :
        print("Veuillez entrer deux nombres valides")

