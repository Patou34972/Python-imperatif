# Tant que ce nombre n’est pas compris entre 1 et 10, le programme redemande un nombre à l’utilisateur.
nombre_utilisateur = int(input("Veuillez saisir un nombre entre 1 est 10 : "))
while nombre_utilisateur <= 0 or nombre_utilisateur > 10:
    nombre_utilisateur = int(input("Veuillez saisir un nombre entre 1 est 10 : "))

# Si le nombre est compris entre 1 et 10, le programme LOGUE ce nombre et se termine.
print(f"le nombre saisi est : {nombre_utilisateur}")


