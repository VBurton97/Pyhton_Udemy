import re
import string
from tinydb import TinyDB, where
from pathlib import Path


class User:

    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent = 4)



    def __init__(self, first_name: str, last_name: str, phone_number: str="",address: str="" ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.adress = address

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name}"


        
    def __str__(self):
        return (f"{self.full_name}\n{self.phone_number}\n{self.adress}")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self):
        return User.DB.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))  # type: ignore

    def _checks(self):
        self._check_names()
        self._check_phone_number
    def _check_phone_number(self):
        phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_number)<10 or not phone_number.isdigit():
            raise ValueError(f"Numéro de téléphone {self.phone_number} invalide.")

    def _check_names(self):
        if not self.first_name+self.last_name :
            raise ValueError("Le prénom et le nom de famille ne peuvent pas être vide")

    def exist(self):
        return bool(self.db_instance)




    def delete(self):       # -> List[int]
        if self.exist():
            return User.DB.remove(doc_ids = [self.db_instance.doc_id]) #type: ignore 

        return[]


    def save(self, validate_data = False):
        if validate_data:
            self._checks()

        User.DB.insert(self.__dict__)  

def get_all_users():
    #for user in User.DB.all():         Explication de la compréhension de liste si dessous
        #each_user = User(**user)

    return[ User(**user) for user in User.DB.all()]  #boucle sous forme de compréhension de liste




if __name__ == "__main__":
#    from faker import Faker
 #   fake = Faker(locale = "fr_FR")
  #  for _ in range(10):
   #     user = User(fake.first_name(),
    #                fake.last_name(),
     #               fake.phone_number(),
      #              fake.address())

#        print(user.save())
 #       print("-"*10)

    Odette = User("Odette", "Paris")
    print(Odette.delete())

    print(type(type))