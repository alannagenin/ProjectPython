from random import randint

#-------------------------------- Choix min max --------------------------------

print("\n-------------- Choix des bornes -------------- ", end='')

borne_inf, borne_sup = int(input("Min : ")), int(input("Max : "))

mon_nombre = randint(borne_inf, borne_sup)
ton_nombre = 0

#-------------------------------- Nb essais --------------------------------

nbr_essais_max = 5
nbr_essais = 1

if borne_sup - borne_inf >= 100:
    nbr_essais_max = randint(6,7)

#-------------------------------- Debut du jeu --------------------------------

print("\nJ'ai choisi un nombre entre ", borne_inf, " et ", borne_sup, ".", sep='')
print("A vous de le deviner en", nbr_essais_max, "tentatives au maximum !")


print("\n-------------- Vos propositions -------------- ")
while ton_nombre != mon_nombre and nbr_essais <= nbr_essais_max:
    print("\nEssai n°",nbr_essais, end='')
    while True:
        try:
            ton_nombre = int(input("Votre proposition : "))
            break
        except ValueError:
            print("Réponse non valide. Réessayez !")
    if ton_nombre < mon_nombre:
        print("Trop petit")
    elif ton_nombre > mon_nombre:
        print("Trop grand")
    else:
        if nbr_essais == 1 :
            print("Bravo ! Vous avez trouvé", mon_nombre, "en", nbr_essais,"essai.")
        else:
            print("Bravo ! Vous avez trouvé", mon_nombre, "en", nbr_essais,"essais.")
    nbr_essais += 1
            
        
if nbr_essais>nbr_essais_max and ton_nombre != mon_nombre :
    print("\nDésolé, vous avez utilisé vos",nbr_essais_max,"essais en vain.")
    print("J'avais choisi le nombre ", mon_nombre,".", end='', sep='')