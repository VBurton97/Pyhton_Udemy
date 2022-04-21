"""###Calculatrice qui demande 2 nombres à l'utilisateur et qui les additionne

#On demande le premier nombre à l'utilisateur qu'on associe à la variable a en s'assurant que a soit comprit comme un entier (int), float si on veut additioner des nombres décimaux.
a = int(input("Entrez un premier nombre : "))

#On demande le deuxième nombre à l'utilisateur qu'on associe à une variable b en s'assurant que b soit comprit comme un entier
b = int(input("Entrez un deuxième nombre : "))

#On effectue l'opération somme

print(f"Le résultat de l'addition de {a} avec {b} est égal à {a+b}")
"""
nombres = range(10)
nombres_pairs = [i for i in nombres if i%2==0]
print(nombres_pairs)
print(<3)