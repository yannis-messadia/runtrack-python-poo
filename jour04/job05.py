import numpy as np
from job04 import Forme, Rectangle

#créer une classe fille :
class Cercle(Forme) :
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def aire(self) :
        return np.pi * self.radius**2

#instancier les classes filles :
rect = Rectangle(2, 4)
print(f"L'air du rectangle est : aire1 = {rect.aire()} cm²")
cercle = Cercle(3)
print(f"L'aire du cercle est : aire 2 = {cercle.aire()}cm²")

## Déja le fait qu'on a importer la classe Rectangle, ça va afficher la valeur de son objet