class Student:
    def __init__(self, nom, prenom, num_etu):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etu = num_etu
        self.__credit = 0 
        self.__level = self.__student_eval()

    def get_credit(self):
        return self.__credit

    def add_credit(self, nombre_ajoute):
        if nombre_ajoute > 0:
            self.__credit += nombre_ajoute
            self.__level = self.__student_eval()
        else:
            print("Veuillez entrer une valeur positive")

    def student_info(self):
        print(f"Étudiant: {self.__prenom} {self.__nom} (N°{self.__num_etu})")
        print(f"Crédits: {self.__credit}")
        print(f"Niveau: {self.__level}")

    def __student_eval(self):
        if self.__credit >= 90:
            return "Excellent"
        elif self.__credit >= 80:
            return "Très bien"
        elif self.__credit >= 70:
            return "Bien"
        elif self.__credit >= 60:
            return "Passable"
        else:
            return "Insuffisant"



etudiant1=Student("Doe","John",145)

etudiant1.add_credit(3)
etudiant1.add_credit(6)
etudiant1.add_credit(99)

print(etudiant1.student_info())