# Exercice 1

for i in range(10):
   # if i % 2 == 0:
        #print(i)

    if i % 2 == 1:
        print(i)


# Exercice 2

# Déclaration de la liste
liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]

# Affichage de tous les nombres de la liste grâce à une boucle
for nombre in liste:
    print(nombre)

# Affichage uniquement des nombres positifs grâce à une boucle combinée à un if
for nombre in liste:
    if nombre > 0:
        print(nombre)

# Trouvez un moyen de calculer le nombre d’éléments positifs et d’afficher ce nombre.
nombre_positif = 0
for nombre in liste:
    if nombre > 0:
        nombre_positif += 1
        print(nombre_positif)


