age_embauche = int(input("age a l'embauche: "))
age_retraite = int(input("age a la retraite "))

erreur_embauche = age_retraite < age_embauche

if not erreur_embauche:
    anciennete = age_retraite - age_embauche
    print("annees de travail: ", anciennete)
else:
    print("erreur")




seq_noms = ("Pier", "Jean", "Jacques")
for nom in seq_noms:
    print("Bonjour", nom, "!")