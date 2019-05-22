#il existe 3 types de variable sous python

variable1 = 5 #integer -> int nombre entier
variable2 = 3.2 # float -> chifre a virgule
variable3 = "yo" # string -> str texte

#Fonction qui permet d'afficher du texte et du contenu d'une variable a l'ecran
print("du texte", variable1, variable2, variable3)

#Fonction permetant de connaitre le type d'une variable
print( type(variable1))

typeDeVariable = type(variable1)
print("le type de la variable1 =", typeDeVariable)

typeDeVariable = type(variable1)
variable1 = str(variable1)
print("le type de la variable1 =", typeDeVariable)

#En python, il existe plusieurs operateur
#addition   > +
#soustraction > -
#multiplication > *
#exposant > **
#dsivision   > /
#division entiere > //
#modulo     > %