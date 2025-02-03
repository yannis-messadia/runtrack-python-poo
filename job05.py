class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def AfficherLesPoints(self):
        print (f'({self.x},{self.y})')

    def afficherX(self):
        print(f'{self.x}')

    def afficherY(self):
        print(f'{self.y}')

    def changerX(self):
        x2 = input(("Entrez ici la nouvelle valeur du point x :"))
        self.x = x2
        print(f'La nouvelle valeur de X est devenue {self.x}')

    def changerY(self):
        y2 = input(("Entrez ici la nouvelle valeur du point Y :"))
        self.y = y2
        print(f'La nouvelle valeur de Y est devenue {self.y}')
        

coordonnees=Point(10,20) #instance des points

coordonnees.AfficherLesPoints()
coordonnees.afficherX()
coordonnees.afficherY()

coordonnees.changerX()
coordonnees.AfficherLesPoints() #on réutilise la méthode Afficher les points pour voir si ça a bien fonctionné

coordonnees.changerY()
coordonnees.AfficherLesPoints() #même logique

#J'initialise les valeurs de x et de y. Ensuite, j'utilise les méthodes demandées pour montrer les coordonnées et les points.
#Pour changer les points X et Y, je demande à l'utilisateur d'input lui même le point voulu que je stocke dans une nouvelle variable, qui remplacera self.x
#Dans ma suite, pour tester mon code, j'utilise la fonction afficherLesPoints.
#Ce code mériterait un contrôle d'erreurs. je peux en effet input des str dans mes nouvelles coordonnées. Voici une suggestion d'un code plus abouti

class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def changer_x(self):
            try:
                self.x = float(input("Entrez ici la nouvelle valeur du point x : "))
                print(f'La nouvelle valeur de X est {self.x}')
            except ValueError:
                print("Erreur. Entrez, s'il vous plait, un nombre.")

    def changer_y(self):
        try:
            self.y = float(input("Entrez ici la nouvelle valeur du point x : "))
            print(f'La nouvelle valeur de X est {self.y}')
        except ValueError:
            print("Erreur. Entrez, s'il vous plait, un nombre.")


    def AfficherLesPoints2(self):
        print (f'({self.x},{self.y})')

coordonnees2 = Point2(10,20)
coordonnees2.changer_x()
coordonnees2.AfficherLesPoints2()

#Ce code serait améliorable en permettant, par exemple, à l'utilisateur d'input lui même directement les valeurs et les utiliser dans les méthodes. 
#En utilisant par exemple Isinstance pour vérifier directement la nature de la valeur proposée et refusant autre chose que des floats ou int.



