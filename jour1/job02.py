class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1=nombre1
        self.nombre2=nombre2
    
    def afficher_operandes(self):
        print(f'Le nombre 1 est {self.nombre1}')
        print(f'Le nombre 2 est {self.nombre2}')

operation = Operation("12", "3")
operation.afficher_operandes()

#Il faut qu'on puisse montrer dans cet exercice les chiffres de l'operation que l'on souhaiterait faire.
#Si les attributs sont les éléments descriptifs des objets d'une classe, les méthodes sont ce que peuvent faire ces objets
#J'ai donc crée une méthode, afficher_operandes, afin de mettre en variable les nombres de ma classe et de les afficher via un print.
#Ensuite, j'instancie et j'utilise afficher_operandes pour obtenir le résultat demandé dans l'exercice.

