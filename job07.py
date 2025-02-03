class Personnage:
    def __init__(self, x=0, y=0, plateau=(10,10)):
        self.x = x
        self.y = y
        self.largeur, self.hauteur = plateau
    
    def gauche(self):
        if self.x>0:
            self.x -= 1
        else:
            print("Je ne peux pas plus me déplacer à gauche, limite atteinte")

    def droite(self):
        if self.x < self.largeur -1:
            self.x += 1
        else:
            print("Je ne peux pas plus me déplacer à droite")

    def bas(self):
        if self.y < self.hauteur+1:
            self.y -= 1
        else:
            print("Bedrock atteinte (Minecraft ref lol)")

    def haut(self):
        if self.y > 0:
            self.y += 1
        else:
            print("Je ne peux pas aller plus haut, je vois d'ici le trou de la couche d'ozone")

    def position(self):
        print((self.x, self.y))  

perso = Personnage(2,0)

perso.gauche()
perso.position()

perso.droite()
perso.position()

perso.bas()
perso.position()

perso.haut()
perso.position()

#Sur pygame, le point 0,0 était en haut à gauche. partant de ce fait, j'ai déterminé les bornes de mon plateau.




