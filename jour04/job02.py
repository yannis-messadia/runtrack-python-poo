from job01 import Personne, Eleve, Professeur

professeur1 = Professeur('maths')
print(professeur1.bonjour())
eleve2 = Eleve()
print(eleve2.allerEnCours())
new_age = eleve2.modifierAge(15)
print(f"Le nouvel age de cet éleve est : {new_age}")