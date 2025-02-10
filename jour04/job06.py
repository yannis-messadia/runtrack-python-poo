#créer la classe :
class Vehicule :
    def __init__(self, marque, modèle,année, prix):
        self.marque = marque 
        self.modèle = modèle
        self.année = année
        self.prix = prix
    
    def informationVehicule(self) :
        return f"Marque = {self.marque}\nModèle = {self.modèle}\nAnnées = {self.année}\nPrix = {self.prix}"
    
    def demarrer(self) :
        return f"Attention, je  roule"
    

#créer  la sous classe Voiture :
class Voiture(Vehicule) :
    def __init__(self, marque, modèle, année, prix, portes = 4):
        super().__init__(marque, modèle, année, prix)
        self.portes = portes

    def informationVehicule(self) :
        return f"Marque = {self.marque} \nModèle = {self.modèle}\nAnnées = {self.année}\nPrix = {self.prix}\nNombre de porte = {self.portes}"
    
    def demarrer(self):    #surcharger une méthode définie dans la classe parent afin qu'il affiche le même message
        return super().demarrer()

#créer la sous classe Moto :   
class Moto(Vehicule) :
    def __init__(self, marque, modèle, année, prix, roue = 2):
        super().__init__(marque, modèle, année, prix)
        self.roue = roue

    def informationVehicule(self) :
        return f"Marque = {self.marque} \nModèle = {self.modèle}\nAnnées = {self.année}\nPrix = {self.prix}\nNombre de roue = {self.roue}"
    
    def demarrer(self):
        return super().demarrer()
   
#instancier les objets :
voiture = Voiture('Mercedes', 'Classe A', 2020, 18500)
print(voiture.informationVehicule())
print(voiture.demarrer())
moto = Moto('Yamaha', '1200 Vmax', 1987, 4500)
print(moto.informationVehicule())
print(moto.demarrer())