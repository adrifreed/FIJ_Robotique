#on a pour depart, un chiffre aleatoir qui est choisi
#apres, le jeu nous demande de taper un nombre entre 0 et100
#si la reponse est inferieur au nombre aleatoir
#il doit afficher "le nombre est plus grand"
#si la reponse est suprieur au nombre aleatoir
#il doit afficher "le nombre est plus petit"
#et sinon vous avez gagner
import random

#initialise nos variables nbAleatoire et trouver
#nbAleatoire sera genere par l'ordinateur
#trouver est un boolean qui est egale a faux
nbAleatoire = random.randrange(0,100)
trouver = False

#Tant que trouver est egale a faux, on continue
while trouver ==False:
    print("tape un nombre entre 0 et 100")
    #on converti le nombre tape au clavier par int
    reponse = int(input())

    #on compare notre reponse avec le nbAleatoire
    if reponse < nbAleatoire :
        print("le nombre est plus grand")
    elif reponse > nbAleatoire :
        print("le nombre est plus petit")
    else : 
        print("gagner")
        #on passe trouver a Vrai pour arreter la boucle
        trouver = True