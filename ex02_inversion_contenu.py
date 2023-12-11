
# Créez une liste appelée listeCopie et copiez tous les éléments de liste dans listeCopie mais dans l’ordre inverse.
liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
liste_copie= liste[:: -1]

# AFFICHEZ l’ensemble des éléments de la liste listeCopie
print("Affichage des éléments de la liste listeCpie:")
for l in liste_copie:
    print(l)

