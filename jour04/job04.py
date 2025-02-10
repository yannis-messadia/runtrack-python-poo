#créer une classe parent :
class Forme :
    def __init__(self):
       pass 
    def aire(self) :
        return 0

#créer une classe enfant   
class Rectangle(Forme) :
    def __init__(self, largeur, hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur
    def aire(self) :     #La classe enfant hérite aussi de la classe parent
        return self.largeur * self.hauteur


#instancier :
rect = Rectangle(2, 4)
print(f"L'aire du rectangle est : aire = {rect.aire()} cm²")   