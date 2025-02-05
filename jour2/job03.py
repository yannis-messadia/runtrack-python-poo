class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

    #accesseurs
    def get_auteur(self):
        return self.__auteur
    
    def get_titre(self):
        return self.__titre
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    #mutateur
    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_nb_pages(self, nouveau_nb_pages):
        if nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Wesh c'est quoi une page négative selon toi ZEBI ?!")

    #verifications et emprunts
    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible=False
            print(f'Vous avez emprunté le livre {self.__titre}')
        else:
            print(f'Ce livre est indisponible')

    def rendre(self):
        if not self.verification():
            self.__disponible=True
            print("Le livre {self.__titre} a bien été rendu")
        else:
            print("Ce livre n'a pas été rendu")
            