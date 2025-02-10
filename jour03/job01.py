class Ville :
    def __init__(self, nom, nb_habitant):
        self.__nom = nom
        self.__nb_habitant = nb_habitant

    def get_ville_name(self) :
        return self.__nom
    
    def get_nb_habitant(self) :
        return self.__nb_habitant
    
    #In order to modify the the number of population, we have 2 choices, we can make a setter or 
       

class Personne(Ville):
    def __init__(self, nom_p, age_p, ville):
        self.__nom_p = nom_p
        self.__age_p = age_p
        self.__ville = ville

    def get_nom(self) :
        return self.__nom_p
    
    def get_age(self) :
        return self.__age_p
    
    def get_ville(self) :
        return self.__ville

    def ajouterPopulation(self) :
        self.__nb_habitant += 1
        return self.__nb_habitant
    
    def afficher_info(self) :
        return f"{self.get_nom()}, {self.get_age()} habitant à {self.get_ville()}"
    
ville1 = Ville('Paris', 1000000)
print(f"La population de la ville de Paris: {ville1.get_nb_habitant()} habitants")
ville2 = Ville('Marseille', 861635)
print(f"La population de la ville de Marseille: {ville2.get_nb_habitant()} habitants")
personne1 = Personne('John', 45, ville1)
personne2 = Personne('Myrtille', 4, ville1)
personne2 = Personne('Chloé', 18, ville2)

print(personne1.afficher_info())
