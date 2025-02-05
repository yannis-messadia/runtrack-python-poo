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

cercle2=Cercle()
cercle2.changerRayon(7)
print(cercle2.diametre())
print(cercle2.circonference())
print(cercle2.aire_cercle())
cercle2.afficherInfos()

#Ce petit programme est un peu procédural à mon gout, mais il fonctionne.
#Inspiré par le job06, j'ai initialisé mon rayon à 0. L'utilisateur change le rayon avec changerRayon, le met à la valeur de son choix (ici 4 pour le premier cercle et 7 pour le second)
#A partir de là, les formules ont été appliquées à la suite. Elles se servent toutes du rayon. Je ne sais pas exactement si je peux aller chercher directement le diamètre pour calculer la circonférence, donc je me base sur diamètre = rayon*2
#Ce programme permet une forme de flexibilité dans le choix de son rayon et sera plus simple que si je crée des instances fixes.
#j'ai du importer math pour sortir pi.

    