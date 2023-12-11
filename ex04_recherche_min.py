# Recherchez le plus petit élément de la liste et AFFICHEZ le.
liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
plus_petit_element = liste[0]
print("le plus petit élément de liste est:")
for l in liste:
    if l < plus_petit_element:
        plus_petit_element = l
print(plus_petit_element)
