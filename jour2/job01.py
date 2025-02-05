class Rectangle:
    def __init__(self, largeur, longueur):
        self.__largeur = largeur
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_largeur(self, nouvelle_largeur):
        if nouvelle_largeur > 0:
            self.__largeur = nouvelle_largeur
        else:
            print("Entrez une valeur positive svp")

    def set_longueur(self, nouvelle_longueur):
        if nouvelle_longueur > 0:
            self.__longueur = nouvelle_longueur
        else:
            print("Entrez une valeur positive :")

    def afficher(self):
        print(f" La longueur du rectangle est de {self.__longueur} et sa largueur est de {self.__largeur}")


rect=Rectangle(10,5)
rect.afficher()

rect.set_largeur(26)
rect.set_longueur(8)
rect.afficher()