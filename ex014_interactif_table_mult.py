# Tant que l’utilisateur ne saisit de nombre compris entre 1 et 10 le programme redemande un nombre
nombre_utilisateur = int(input("Veuillez saisir un nombre entre 1 est 10 : "))
while nombre_utilisateur <= 0 or nombre_utilisateur > 10:
    nombre_utilisateur = int(input("Veuillez saisir un nombre entre 1 est 10 : "))

# Si le nombre est bien entre 1 et 10, le programme LOGUE la table de multiplication de ce nombre puis s’arrête.
print(f"la table de multiplication de {nombre_utilisateur}: {nombre_utilisateur}*")
for i in range(1, 11):
    resultat = nombre_utilisateur * i
    print(f"{nombre_utilisateur} * {i} = {resultat}")
