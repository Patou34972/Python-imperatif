
def nombre_entiers(liste):
    total_entiers = 0

    for element in liste:
        if isinstance(element, int):
            # Si l'élément est un entier, incrémenter le total
            total_entiers += 1
        elif isinstance(element, list):
            # Si l'élément est une sous-liste, appeler la fonction récursivement
            total_entiers += nombre_entiers(element)

    return total_entiers

# Exemple d'utilisation
exemple_liste = [28, [12, [13, 1], -2, [[4, 5], -5]]]
resultat = nombre_entiers(exemple_liste)
print("Le nombre d'entiers dans la liste est :", resultat)
