
# AFFICHEZ l’ensemble des éléments de la liste grâce à une boucle
liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
print("Affichage des élements de liste :")
for l in liste:
    print(l)

# AFFICHEZ l’ensemble des éléments de la liste dans l’ordre inverse
print("Affichage des éléments dans l'ordre inverse")
for l in range(len(liste)-1, -1, -1):
    print(liste[l])
