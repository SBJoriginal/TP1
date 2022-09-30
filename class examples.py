#age_embauche = int(input("age a l'embauche: "))
#age_retraite = int(input("age a la retraite "))

#erreur_embauche = age_retraite < age_embauche

#if not erreur_embauche:
 #   anciennete = age_retraite - age_embauche
  #  print("annees de travail: ", anciennete)
#else:
 #   print("erreur")




#seq_noms = ("Pier", "Jean", "Jacques")
#for nom in seq_noms:
 #   print("Bonjour", nom, "!")

def valider_date(message, nb_characteres):
    quantite = input(message)
    while not (quantite.isnumeric() and len(quantite) == nb_characteres):
        print("invalid. ")
        quantite = input(message)
    return quantite

jour = valider_date("Quel jour sommes-nous (jj)? ", 2)
mois = valider_date("Quel mois sommes-nous (mm)? ", 2)
annee = valider_date("Quel annee sommes-nous (aaaa)? ", 4)

print("nous somme le", jour,"/", mois,"/", annee,"/")






def diviseur(a, b):
    return a % b == 0

def pair (n):
    return diviseur(n,2)

print(pair(142))