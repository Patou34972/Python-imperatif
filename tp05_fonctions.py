#EXERCICE EX01_SOMME_NB_PAIRS
#Réalisez une fonction qui retourne la somme des nombres pairs d’une liste
def somme_nombres_pairs(liste):
    somme = 0

    for nombre in liste:
        if nombre % 2 == 0:  # Vérifie si le nombre est pair
            somme += nombre

    print("Liste :", liste)
    print("Somme des nombres pairs :", somme)
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somme_nombres_pairs(ma_liste)


#EXERCICE EX02_PALINDROME
#Réalisez une fonction qui retourne si oui ou non la chaine de caractères passée en paramètre est un palindrome
def est_palindrome(chaine):
  for i in range(len(chaine)//2):
    if chaine[i] != chaine[-i-1]:
        return False
  return True

print("bob : palindrome = ", est_palindrome("bob"))
print("boby : palindrome = ", est_palindrome("boby"))


#EXERCICE EX03_RECHERCHEMINMAX
#Réalisez une fonction qui prend 3 paramètres : un min, un max et une liste
def recherche_min_max(minimum, maximum, liste):
    resultats = []
    for nombre in liste:
        if minimum <= nombre <= maximum:

            resultats.append(nombre)
    return resultats

liste_originale = [1, 5, 10, 15, 20, 25, 30]
valeur_minimale = 10
valeur_maximale = 25
resultats = recherche_min_max(valeur_minimale, valeur_maximale, liste_originale)
print("Liste d'origine :", liste_originale)
print("Liste entre", valeur_minimale, "et", valeur_maximale, ":", resultats)




#EXERCICE EX04_CALCULMOYENNE
#Réalisez une fonction qui calcule la moyenne des éléments d’une liste
def calcul_moyenne(liste):

    if not liste:
        print("La liste est vide. Impossible de calculer la moyenne.")
        return None
    somme = 0
    nombre_elements = 0

    for element in liste:
        if isinstance(element, (int, float)):
            somme += element
            nombre_elements += 1
        else:
            print(f"Attention: L'élément {element} n'est pas un nombre et sera ignoré.")
    if nombre_elements == 0:
        print("Aucun élément numérique trouvé dans la liste. Impossible de calculer la moyenne.")
        return None

    moyenne = somme / nombre_elements

    return moyenne

liste_de_nombres = [10, 15, 20, 25, 30]

resultat_moyenne = calcul_moyenne(liste_de_nombres)

if resultat_moyenne is not None:
    print("Liste de nombres :", liste_de_nombres)
    print("Moyenne des éléments :", resultat_moyenne)

