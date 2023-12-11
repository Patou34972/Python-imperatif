# Créer une liste resultat dont chaque élément est la somme des éléments des liste 1 et 2 de même index.
liste1 = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
liste2 = [-1, 12, 17, 14, 5, -9, 0, 18, -6, 0, 4, -13, 5, 7, -2, 8, -1]
liste_resultat = []

liste_resultat = resultat = [x + y for x, y in zip(liste1, liste2)]

# AFFICHEZ les valeurs de la liste somme avec une boucle.
print("Affichage des valeurs de liste somme: ")
for element in liste_resultat:
    print(element)
