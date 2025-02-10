# creation de la classe
class Personne  : 
    def __init__(self, age = 14):
        self.age = age 

    def afficherAge(self) :
        return f"L'age de la personne est : {self.age}"
    
    def bonjour(self) :
        return f"Hello"
    
    def modifierAge(self, new_value) :
        if new_value > 0 :
            self.age = new_value
        return self.age
    

# creation de la sous classe 
class Eleve(Personne) :
    def __init__(self):
        super().__init__(age = 14)

    def allerEnCours(self) :
        return f"Je vais en cours"
    
    def afficherAge(self) :
        return f"J'ai {self.age} ans"
    
class Professeur(Personne) :
    def __init__(self, matièreEnseignee):   #il faut mettre les attribut qui sont initialisés par défaut a la fin
        super().__init__(age = 14)
        self.__matièreEnseignee = matièreEnseignee

    def enseigner(self) :
        return f"Le cours va commencer"
    
    def get_matière(self) :
        return self.__matièreEnseignee
    
    def set_matière(self, new_matiere) :
        self.__matièreEnseignee = new_matiere
        return self.__matièreEnseignee
    
#instancitaion des classes
personne1 = Personne()
eleve1 = Eleve()
#Afficher la valeur iitialisée par défaut
print(eleve1.afficherAge())