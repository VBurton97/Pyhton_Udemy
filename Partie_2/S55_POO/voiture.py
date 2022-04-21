from dataclasses import dataclass

@dataclass
class voiture :
    essence: int = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d'essence")


    def roule(self, km):
        if km > 2000:
            print("Votre voiture ne fera jamais un tel trajet avec un seul plein! Veuillez roulez moins et faire le pleins en chemin.")

        elif self.essence >0 and (self.essence - ((km*5)/100)) >= 0 :
            self.essence -= (km*5)/100

            if self.essence < 10:
                print("Vous n'avez bientôt plus d'essence")    
            self.afficher_reservoir()
            
        elif self.essence >0 and (self.essence - ((km*5)/100)) <= 0:
            print("Vous n'avez pas suffisament d'essence pour faire cette distance. Roulez moins ou faite le plein")

        elif self.essence <= 0 :
            print("Vous n'avez plus d'essence, faites le plein!")

    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")

        





        

