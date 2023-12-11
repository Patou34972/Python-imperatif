# AFFICHEZ le nombre de valeurs communes aux 2 listes. On peut déjà voir que les valeurs 3 et 8 sont communes aux 2 listes, mais combien y en a-t-il au total ?

liste1 = [1, 15, -3, 8, 7, 4, -2, 28, -1, 17, 2, 3, 0, 14, -4]
liste2 = [3, -8, 17, 5, -1, 4, 0, 6, 2, 11, -5, -4, 8]

nombre_valeurs_communes = 0

for element in liste1:
    if element in liste2:
        nombre_valeurs_communes += 1

print("Le nombre de valeurs communes aux deux listes est :", nombre_valeurs_communes)
