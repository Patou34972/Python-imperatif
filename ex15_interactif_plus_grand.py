# demande 10 nombres à un utilisateur
liste = []
for i in range(10):
    nombre_utilisateur = float(input(f"Veuillez saisir le nombres {1 + 1} : "))
    liste.append(nombre_utilisateur)

plus_grand_nombre = liste[0]
for n in liste:
    if n > plus_grand_nombre:
        plus_grand_nombre = n
print(f"les plus grand nombre parmi les saisies est : {plus_grand_nombre}")


