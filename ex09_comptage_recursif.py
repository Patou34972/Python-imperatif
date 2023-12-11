def nombre_elements_dans_plage(liste, valeur_min, valeur_max):
    total_elements_dans_plage = 0

    for element in liste:
        if isinstance(element, int):
            # Si l'élément est un entier, vérifier s'il est dans la plage spécifiée
            if valeur_min <= element <= valeur_max:
                total_elements_dans_plage += 1
        elif isinstance(element, list):
            # Si l'élément est une sous-liste, appeler la fonction récursivement
            total_elements_dans_plage += nombre_elements_dans_plage(element, valeur_min, valeur_max)

    return total_elements_dans_plage

# Exemple d'utilisation
exemple_liste = [28, [12, [13, 1], -2, [[4, 5], -5]]]
valeur_min = 10
valeur_max = 15
resultat = nombre_elements_dans_plage(exemple_liste, valeur_min, valeur_max)
print(f"Le nombre d'éléments compris entre {valeur_min} et {valeur_max} est :", resultat)
