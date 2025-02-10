#créer une classe :
class Rectangle :
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    #Afin de pouvoir acceder aux attributs de Rectangle et modifier leurs valeurs, on doit créer un getter et uun settter
    def getter_r_longueur(self) :
        return self.__longueur
    
    def getter_r_largeur(self) :
        return self.__largeur
    
    def set_longueur(self, new_longueur) :
        if new_longueur > 0 :
            self.__longueur = new_longueur
        return self.__longueur

    def set_largeur(self, new_largeur) :
        if new_largeur > 0 :
            self.__largeur = new_largeur
        return self.__largeur

    def perimetre(self) :
        return (self.__largeur + self.__longueur) * 2
    
    def surface(self) :
        return self.__longueur * self.__largeur
    
class Parallelepipede(Rectangle) :
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self) :
        return self.surface() * self.hauteur

rect = Rectangle(3, 4)
print(rect.getter_r_largeur())
print(rect.getter_r_longueur())
para = Parallelepipede(3, 4, 5)
print(para.volume())