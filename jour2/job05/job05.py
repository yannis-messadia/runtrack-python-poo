class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        """Initialise une voiture avec ses informations et un réservoir par défaut à 50L."""
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50  # Initialisation du réservoir à 50L

    # Accesseurs (Getters)
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs (Setters)
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        if kilometrage >= 0:
            self.__kilometrage = kilometrage
        else:
            print("Erreur : Le kilométrage ne peut pas être négatif.")

    def set_reservoir(self, litres):
        if 0 <= litres <= 50:
            self.__reservoir = litres
        else:
            print("Erreur : Le réservoir doit être compris entre 0 et 50 litres.")

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        """Retourne la quantité de carburant dans le réservoir."""
        return self.__reservoir

    # Méthodes pour démarrer et arrêter la voiture
    def demarrer(self):
        """Démarre la voiture si le réservoir contient plus de 5L de carburant."""
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Impossible de démarrer : Réservoir presque vide.")

    def arreter(self):
        """Arrête la voiture."""
        self.__en_marche = False
        print("La voiture est arrêtée.")

    # Méthode pour afficher les informations de la voiture
    def afficher_infos(self):
        """Affiche les informations de la voiture."""
        etat = "en marche" if self.__en_marche else "à l'arrêt"
        return (f"Voiture: {self.__marque} {self.__modele} ({self.__annee})\n"
                f"Kilométrage: {self.__kilometrage} km\n"
                f"Réservoir: {self.__reservoir} L\n"
                f"État: {etat}")


# Instanciation d'une voiture
voiture1 = Voiture("Toyota", "Corolla", 2020, 30000)

# Affichage des informations avant de démarrer
print(voiture1.afficher_infos())

# Tentative de démarrage
voiture1.demarrer()
print(voiture1.afficher_infos())

# Réduction du réservoir et nouvelle tentative de démarrage
voiture1.set_reservoir(4)
voiture1.demarrer()

# Arrêt de la voiture
voiture1.arreter()
print(voiture1.afficher_infos())
