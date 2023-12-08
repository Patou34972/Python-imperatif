number = 12
decimal = 12.5
string = "Michel"
boolean = True
print("Magaly a eu une note de " + str(number) + "/20 en Histoire et Geographie")
print("la valeur est de type", type(number))

print("La bouteille de vin du Pic saint Loup coûte " + str(decimal) + " euros")
print("la valeur est de type", type(decimal))

print("Comment vas-tu " + string + " ?")
print("la valeur est de type", type(string))

print("La valeur de ma variable boolean est :", boolean)
print("la valeur est de type", type(boolean))

resultat = f"Monsieur {string} a eu une note de {number} sur 20 et une moyenne générale de {decimal}"
print(resultat)
