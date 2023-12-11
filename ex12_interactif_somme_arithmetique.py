nombre_utilisateur = int(input("Veuillez saisir un nombre : "))

# Initialiser la variable de somme
somme = 0

# Calculer la somme des entiers de 1 à ce nombre
for i in range(1, nombre_utilisateur + 1):
    somme += i

# Afficher la somme des entiers de 1 à ce nombre
print(f"La somme des entiers de 1 à {nombre_utilisateur} inclus est : {somme}")
