class Part:
    def __init__(self, name, materiel):
        self.name = name
        self.materiel = materiel

    def change_material(self,new_materiel):
        self.materiel = new_materiel
        return self.materiel

    def __str__(self):
        return f'{self.name}, en {self.materiel}'
        

class Ship:
    def __init__(self, name):
        self.name=name
        self.__parts = {
            "Piece1": Part("caca", "Bois")
        }

    def display_state(self):
        print(f"Ship {self.name}")
        for part in self.__parts:
            print(f' {self.__parts}')
        
    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name]=new_part
            print(f"{part_name} a été remplacé par un(e) {new_part}")
        else:
            print("Erreur")

ship1 = Ship("Yannis")
part1 = Part("Gouvernail", "Bois")

ship1.display_state()
ship1.replace_part("Piece1", "Mat")
ship1.display_state()
