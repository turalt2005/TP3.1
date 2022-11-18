# Troy Tural 404
# TP3

import random

Quit = 'n'
while Quit == 'n':
    x = random.randint(1, 5)
    y = random.randint(1, 6)
    z = random.randint(1, 6)
    nb_vies = 20
    print("Bienvenue! Dans ce jeu, tu auras 20 vies pour combattre le plus de monstres possible."
          "Pour réussir un combat, il faut que la valeur du dé que tu lance  soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
          "Une défaite a lieu lorsque la valeur du dé lancé  est inférieure ou égale à la force de l’adversaire.  Par exemple, tes nbrs de vies est diminué de la force de l’adversaire a cause que le resultat de ton lancé est inferieur au vies de l'énnemi."
          "La partie se termine lorsque tes points de vie  tombent sous 0."
          "-Cliquez sur 1 un pour combattre un ennemi"
          "-Cliquez sur 2 pour vous échapper d'un ennemi"
          "Cliquez sur 3 pour reouvrir ce menu"
          "Cliquez sur 4 pour quitter la partie"
          "Bonne Chance!")

    choix = input("Que voulez-vous faire ? "
                  "1- Combattre cet adversaire"
                  "2- Contourner cet adversaire et aller ouvrir une autre porte"
                  "3- Afficher les règles du jeu"
                  "4- Quitter la partie")
    if choix = 1:

