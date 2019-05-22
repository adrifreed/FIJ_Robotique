#il existe 2 types de boucles
#while > tant que...
#avec un compteur qui diminue chaque tour
compteur = 10
while compteur >= 0:
    print ("le cours est fini dans :", compteur)
    compteur = compteur - 1

#avec un boolean
flag = True

while flag:
    print("bonjour")
    flag = False 

#For > pour chaque 
phrase = "Bonjour a tous !"

for lettre in phrase:
    print(lettre)