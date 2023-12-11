# Calculez et AFFICHEZ la moyenne des valeurs de la liste.
liste = [1, 15, -3, 0, 8, 7, 4, -2, 28, 7, -1, 17, 2, 3, 0, 14, -4]
somme = 0
nombre_elements = 0
print("La moyenne des valeurs de la liste est de:")

for element in liste:
    somme += element
    nombre_elements += 1
    moyenne = somme // nombre_elements
print(moyenne)

# Calculez et AFFICHEZ la moyenne des valeurs positives de la liste uniquement.

print("La moyenne des valeurs positives  de la liste est de:")
for element in liste:
    if element > 0:
        somme += element
        nombre_elements += 1
        moyenne_positive = somme // nombre_elements
print(moyenne_positive)
