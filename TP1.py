#Configuration de la pompe à essence
prix_essence_ordinaire = float(input("Quel est le prix de l’essence ordinaire en ($/L) : "))
prix_essence_diesel = float(input("Quel est le prix de l’essence diesel en ($/L) : "))
prix_essence_super = (prix_essence_ordinaire * 1.1)
code_secret_du_jour = input("Quel est le code secret du jour : ")
choix_dessence = False

print(prix_essence_ordinaire)
print(prix_essence_diesel)
print(code_secret_du_jour)

print("∗∗∗∗∗∗∗∗∗∗\n"
      "une automobile arrive.")
#Arrivée d’une automobile
litre_dans_le_reservoir_total = float(input("La nombre de litres total de ton réservoir est : "))
litre_dans_le_reservoir_avant = float(input("La nombre de litres actuel de ton rérsvoir est : ")) #make sure its lower then total
print("La nombre de litres total de ton réservoir est : ", litre_dans_le_reservoir_total, "\n"
      "et il en contient actuellement : ", litre_dans_le_reservoir_avant)

#Demander le type d’essence
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
      "- - -                                 Affichage sur la pompe                                             - - -\n"
      "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
      "Veuillez sélectionner le type d'essence parmi : \n"
      "-  [O] ordinaire : ",prix_essence_ordinaire, "$ / litre \n"
      "-  [S] uper : ",prix_essence_super, "$ / litre \n"
      "-  [D] iesel : ",prix_essence_diesel, "$ / litre ")

while choix_dessence == False:
      essence_type = input("Votre choix (O, S, D) : ")
      if (essence_type == "O"):
            choix_dessence = True
      else:
            if (essence_type == "S"):
                  choix_dessence = True
            else:
                  if (essence_type == "D"):
                        choix_dessence = True
                  else:
                        print("Cela est un choix invalid! Veuillez essayer encore S.V.P!")
print("thanks!")


#Demander le plein ou un montant fixe
plein_ou_fixe = input("Souhaitez-vous faire le plein (P) ou choisir un montant fixe (M) ? ")
input("Remplissage !")
#Remplissage litre par litre
#Entrer un code promotionnel
#Affichage final