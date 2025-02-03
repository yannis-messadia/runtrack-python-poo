import math

class Cercle:
    def __init__(self):
        self.rayon = 0
        self.diam = " "
        self.circo = " "
        self.aire = " "
        

    def changerRayon(self, rayon):
        self.rayon = rayon
        print(f"Le nouveau rayon est de {self.rayon}")
    
    def diametre(self):
        self.diam = 2*self.rayon
        return self.diam

    def circonference(self):
        self.circo=2*self.rayon*math.pi
        return self.circo
    
    def aire_cercle(self):
        self.aire=math.pi*(self.rayon)**2
        return self.aire
    
    def afficherInfos(self):
        print(f"rayon = {self.rayon}/diametre = {self.diam}/circonference = {self.circo}/aire = {self.aire}")

cercle=Cercle()
cercle.changerRayon(4)
print(cercle.diametre())
print(cercle.circonference())
print(cercle.aire_cercle())
cercle.afficherInfos()
    