class Produit:
    def __init__(self, nom, prixHT, TVA=0.1):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1+self.TVA) #ajoute 20% au prix, soit la TVA
    
    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom
    
    def modifier_prixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def afficher(self):
        return f"Produit: {self.nom} ; Prix HT: {self.prixHT} EUR ; TVA: {self.TVA*100}% ; Prix TTC:{self.CalculerPrixTTC()} EUR"
    
produit1=Produit("Kebab", 6.50)
produit2=Produit("Fajitas", 9.50)

print(produit1.afficher())
print(produit2.afficher())

produit1.modifier_nom("Tacos")
produit1.modifier_prixHT(8)

print(produit1.afficher())

#Dans ma fonction constructeur, je demande le nom du produit et son prix hors taxe pour faire les opérations
#J'ai choisi de faire mon job sur les produits de consommation immédiate type kebab et vente à emporter. La TVA est fixée à 10% dans ce cas.
#Des tests ont été effectués pour chacune des fonction : tout marche
#On va essayer avec un produit comme un bonnet, ayant une TVA de 20%, pour voir

produit3 = Produit("Bonnet", 10, 0.2)
print(produit3.afficher())

#ça marche : je peux modifier ma TVA grâce à la construction de ma classe
#nouveauté par rapport aux jobs précédents : j'utilise dans mon print la méthode CalculerprixTTC, me permettant de faire mon exercice en moins de lignes.