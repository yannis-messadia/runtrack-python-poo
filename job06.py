class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = " "
    
    def afficher_age(self):
        print(f"L'âge de l'animal est de {self.age}")

    def vieillir(self):
        self.age += 1
    
    def nommer(self, nom): #on met nom en paramètre car on va l'ajouter aux attributs nécessaires. Pour marcher, en utilisant cette méthode, on va devoir ajouter le nom entre guillemets
        self.prenom = nom


animal=Animal()
animal.afficher_age()

#Ici, on retire en paramètre l'âge et le prénom, car on instancie l'age à zéro directement dans la classe.
#ça nous permet d'avoir l'âge à 0 même si on ne le dit pas clairement dans notre instance

animal.vieillir()
animal.afficher_age()

#On ajoute un an à self.age et on vérifie avec afficher age.

animal.nommer("Luna")
print(f"Le nom de l'animal est devenu {animal.prenom}") #on vérifie en appelant animal.prenom au lieu de self.prenom car on est en dehors de la classe et dans une instance



