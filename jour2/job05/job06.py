class Commande:
    def __init__(self, numero_commande):
        """Initialise une commande avec un numéro, une liste de plats vide et un statut 'en cours'."""
        self.__numero_commande = numero_commande
        self.__plats = {}  # Dictionnaire pour stocker {nom_du_plat: prix}
        self.__statut = "en cours"  # Statut par défaut

    # Accesseurs (getters)
    def get_numero_commande(self):
        return self.__numero_commande

    def get_statut(self):
        return self.__statut

    def get_plats(self):
        return self.__plats.copy()  # Renvoie une copie pour éviter la modification externe

    # Méthode pour ajouter un plat
    def ajouter_plat(self, nom_plat, prix):
        """Ajoute un plat à la commande si elle est encore en cours."""
        if self.__statut == "en cours":
            if prix > 0:
                self.__plats[nom_plat] = prix
                print(f"Le plat '{nom_plat}' a été ajouté à la commande.")
            else:
                print("Erreur : Le prix du plat doit être supérieur à zéro.")
        else:
            print("Impossible d'ajouter un plat : la commande n'est plus en cours.")

    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        """Calcule le total des plats commandés (sans TVA)."""
        return sum(self.__plats.values())

    # Méthode pour calculer la TVA
    def calculer_TVA(self, taux_TVA=0.2):
        """Calcule la TVA à partir du total (par défaut 20%)."""
        return self.__calculer_total() * taux_TVA

    # Méthode pour afficher les informations de la commande
    def afficher_commande(self):
        """Affiche les détails de la commande avec le total TTC."""
        if not self.__plats:
            print("La commande est vide.")
            return

        print(f"\nCommande N°{self.__numero_commande} - Statut : {self.__statut}")
        for plat, prix in self.__plats.items():
            print(f" - {plat}: {prix:.2f}€")

        total_HT = self.__calculer_total()
        total_TVA = self.calculer_TVA()
        total_TTC = total_HT + total_TVA

        print(f"\nTotal HT: {total_HT:.2f}€")
        print(f"TVA (20%): {total_TVA:.2f}€")
        print(f"Total TTC: {total_TTC:.2f}€\n")

    # Méthode pour annuler la commande
    def annuler_commande(self):
        """Annule la commande si elle est encore en cours."""
        if self.__statut == "en cours":
            self.__statut = "annulée"
            self.__plats.clear()  # Supprime tous les plats
            print("La commande a été annulée.")
        else:
            print("Impossible d'annuler : la commande est déjà terminée ou annulée.")

    # Méthode pour terminer la commande
    def terminer_commande(self):
        """Termine la commande et la valide définitivement."""
        if self.__statut == "en cours":
            self.__statut = "terminée"
            print("La commande a été terminée.")
        else:
            print("Impossible de terminer : la commande est déjà annulée ou terminée.")


# === Exemple d'utilisation ===
commande1 = Commande(101)

# Ajout de plats
commande1.ajouter_plat("Pizza Margherita", 12.5)
commande1.ajouter_plat("Pâtes Carbonara", 14.0)
commande1.ajouter_plat("Tiramisu", 6.0)

# Affichage des détails de la commande
commande1.afficher_commande()

# Tentative d'annulation
commande1.annuler_commande()
commande1.afficher_commande()  # Vérifier que la commande a bien été annulée

# Nouvelle commande
commande2 = Commande(102)
commande2.ajouter_plat("Sushi", 18.0)
commande2.ajouter_plat("Ramen", 13.5)

commande2.afficher_commande()

# Terminer la commande
commande2.terminer_commande()
commande2.afficher_commande()

# Essai d'ajouter un plat après la validation (devrait échouer)
commande2.ajouter_plat("Mochi", 5.0)
