class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.nom} {self.prenom}"
    
personne1= Personne("John", "Doe")
print(personne1.SePresenter())

#la logique est la même qu'au job précédent. Dans ma fonction constructeur, je mets les attributs.
#Je demande à la méthode de me retourner une phrase utilisant mon plan de classe.
#j'utilise print pour avoir l'affichage sur mon terminal.