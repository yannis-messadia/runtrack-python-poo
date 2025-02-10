class Part :
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material) :
        self.material = new_material
        return self.material
    
    def __str__(self):
        return f"({self.name}, {self.material})"
  
class Ship:   #je vais la considérer comme une classe parent et non pas sous-classe
    def __init__(self, nom):
        self.nom = nom
        self.__parts = {
            'Part1' : Part('Coque', 'Bois'),   #c'est possibled'appeler une classe dans une classe
            'Part2' : Part('Helice', 'Fer')
                        }  #j'ai initialisé mon dictionnaire

    def display_part(self) :
        for  piece in self.__parts :
            print(piece)   #lister les pièces du bateau (les clés du dictionnaires)
        
    def replace_part(self, part_name, new_part) :
        if part_name in self.__parts :
            self.__parts[part_name] = new_part     #remplacer la premiere valeur de la clé
            for i, j in self.__parts.items() :
                print(i,j)
        else :
            print(f"Cette pièce n'existe pas !")  

    # def change_part(self, part_name, new_material) :
    #     if part_name in self.__part :
    #         self.__part[part_name] = new_material
    #         print(f"La nouvelle piece est en {new_material}")
    #     else :
    #         print(f"La pièce n'existe pas")


#créer un objet :
#part1 = Part('Mat', 'Bois') 
ship1 = Ship('Yannis')
print(ship1.display_part())
ship1.replace_part('Coque', 'Amina')
