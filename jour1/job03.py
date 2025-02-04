class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1=nombre1
        self.nombre2=nombre2
    
    def addition(self):
        sum = self.nombre1 + self.nombre2
        print(f"le résultat de l'addition est {sum}")
        

operation = Operation(12, 3)
operation.addition()

#l'addition est une possibilité d'action de notre classe, donc une méthode
#je mets dans une variable le résultat de l'addition entre le nombre 1 et le nombre 2 et je le print.
#Je m'assure que les deux nombres soient perçus comme des int pour permettre une opération mathématique en retirant les guillemets.