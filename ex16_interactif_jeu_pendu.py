import random

# Liste de mots possibles
mots = ["python", "programmation", "pendu", "jeu", "informatique", "algorithmique"]

# Choix aléatoire d'un mot
mot_a_deviner = random.choice(mots)

# Initialisation du mot masqué
mot_masque = ["_"] * len(mot_a_deviner)

# Initialisation des variables
erreurs_max = random.randint(5, 10)
erreurs_actuelles = 0
lettres_proposees = []

# Fonction pour afficher le mot masqué
def afficher_mot():
    print(" ".join(mot_masque))

# Boucle principale du jeu
while True:
    afficher_mot()
    print(f"Erreurs restantes : {erreurs_max - erreurs_actuelles}")
    lettre = input("Proposez une lettre : ").lower()

    # Vérifier si la lettre a déjà été proposée
    if lettre in lettres_proposees:
        print("Vous avez déjà proposé cette lettre. Veuillez en choisir une autre.")
        continue

    lettres_proposees.append(lettre)

    # Vérifier si la lettre est dans le mot à deviner
    if lettre in mot_a_deviner:
        print("Bonne devinette !")
        for i in range(len(mot_a_deviner)):
            if mot_a_deviner[i] == lettre:
                mot_masque[i] = lettre
    else:
        print("La lettre n'est pas dans le mot.")
        erreurs_actuelles += 1

    # Vérifier les conditions de victoire ou de défaite
    if erreurs_actuelles == erreurs_max:
        print("Désolé, vous avez perdu. Le mot était :", mot_a_deviner)
        break
    elif "_" not in mot_masque:
        print("Félicitations, vous avez trouvé le mot ! Le mot était :", mot_a_deviner)
        break
