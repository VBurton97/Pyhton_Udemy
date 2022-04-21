with open("/Users/victor/Info/Python_Udemy/Partie_2/S40_Organiser_des_donnees/prenom.txt", "r") as f:
    lines = f.read().splitlines()
    print(lines)

prenoms = []
for line in lines:
    prenoms.extend(line.split())
    print(prenoms)

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

with open("/Users/victor/Info/Python_Udemy/Partie_2/S40_Organiser_des_donnees/prenom.txt", "w") as f:
    f.write("\n".join(sorted(prenoms_final)))








