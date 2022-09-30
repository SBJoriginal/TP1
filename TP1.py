#Configuration de la pompe à essence
prix_essence_ordinaire = float(input("Quel est le prix de l’essence ordinaire en ($/L) : "))
prix_essence_diesel = float(input("Quel est le prix de l’essence diesel en ($/L) : "))
prix_essence_super = (prix_essence_ordinaire * 1.1)
code_secret_du_jour = input("Quel est le code secret du jour : ")
choix_dessence = False
choix_plein_ou_fixe = False
mettre_essence = True
mettre_l = 0
mettre_1l = 0
mettre_moins_de_1l = 0
prix_gas = 0
final_l = 0
final_liter_price = 0
lire_dans_le_reservoir_fixe = 0
O = prix_essence_ordinaire
S = prix_essence_super
D = prix_essence_diesel

#DONT FORGET TO REMOVE THIS WHEN YOUR FINISHED
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
      "-  [S] uper : ",round(prix_essence_super, 2), "$ / litre \n"
      "-  [D] iesel : ",prix_essence_diesel, "$ / litre ")

while choix_dessence == False:
      essence_type = input("Votre choix (O, S, D) : ")
      if essence_type.lower() == "o":
            choix_dessence = True
      else:
            if (essence_type.lower() == "s"):
                  choix_dessence = True
            else:
                  if (essence_type.lower() == "d"):
                        choix_dessence = True
                  else:
                        print("Cela est un choix invalid! Veuillez essayer encore S.V.P!")




#Demander le plein ou un montant fixe
while choix_plein_ou_fixe == False:
      plein_ou_fixe = input("Souhaitez-vous faire le plein (P) ou choisir un montant fixe (M) ? ")
      if (plein_ou_fixe == "P"):
            choix_plein_ou_fixe = True
      else:
            if (plein_ou_fixe == "M"):
                  choix_plein_ou_fixe = True
            else:
                  print("Cela est un choix invalid! Veuillez essayer encore S.V.P!")

print("Remplissage!") #need to account for negative numbers
litre_en_mettant_le_gas = litre_dans_le_reservoir_avant
while mettre_essence == True:
      if (plein_ou_fixe == "P"):
            mettre_l = input("Appuyez sur entrée pour ajounter un litre (A pour arrêter).")
            if (mettre_l == ""):
                  #if number is at least 1.9 away the first condition clears and then the second as well
                  if (litre_en_mettant_le_gas < litre_dans_le_reservoir_total) and (litre_en_mettant_le_gas > litre_dans_le_reservoir_total - 1):
                        mettre_moins_de_1l = mettre_moins_de_1l + 1
                        print("mettre_moins_de_1l", mettre_moins_de_1l)
                        final_l = litre_dans_le_reservoir_total - litre_en_mettant_le_gas

                        if (essence_type == "O"):
                              final_liter_price = final_l * prix_essence_ordinaire
                              prix_gas = prix_gas + final_liter_price
                              litre_en_mettant_le_gas = litre_en_mettant_le_gas + final_l
                              print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur", litre_dans_le_reservoir_total, "\n"
                                    "Coût (jusqu'à maintenant) : ", prix_gas, "$")
                        else:
                              if (essence_type == "D"):
                                    final_liter_price = final_l * prix_essence_diesel
                                    prix_gas = prix_gas + final_liter_price
                                    litre_en_mettant_le_gas = litre_en_mettant_le_gas + final_l
                                    print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur", litre_dans_le_reservoir_total, "\n"
                                          "Coût (jusqu'à maintenant) : ", prix_gas, "$")
                              else:
                                    if (essence_type == "S"):
                                          final_liter_price = final_l * prix_essence_super
                                          prix_gas = prix_gas + final_liter_price
                                          litre_en_mettant_le_gas = litre_en_mettant_le_gas + final_l
                                          print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",litre_dans_le_reservoir_total, "\n"
                                                "Coût (jusqu'à maintenant) : ", prix_gas, "$")
                  if (litre_en_mettant_le_gas + 1 <= litre_dans_le_reservoir_total):
                        mettre_1l = mettre_1l + 1
                        print("mettre_l", mettre_l)
                        litre_en_mettant_le_gas = litre_en_mettant_le_gas + 1
                        if (essence_type == "O"):
                              prix_gas = prix_gas + prix_essence_ordinaire
                              print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",litre_dans_le_reservoir_total, "\n"
                                    "Coût (jusqu'à maintenant) : ", prix_gas, "$")
                        else:
                              if (essence_type == "D"):
                                    prix_gas = prix_gas + prix_essence_diesel
                                    print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",litre_dans_le_reservoir_total, "\n"
                                          "Coût (jusqu'à maintenant) : ", prix_gas, "$")
                              else:
                                    if (essence_type == "S"):
                                          prix_gas = prix_gas + prix_essence_super
                                          print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",litre_dans_le_reservoir_total, "\n"
                                                "Coût (jusqu'à maintenant) : ", prix_gas,"$")
                  if (litre_en_mettant_le_gas >= litre_dans_le_reservoir_total):
                        mettre_essence = False
            if (mettre_l == "A"):
                  mettre_essence = False














      if (plein_ou_fixe == "M"):
            total_prix_desirer = float(input("Veuillez inscrire le montant souhaité : "))
            mettre_l = input("Appuyez sur entrée pour ajounter un litre (A pour arrêter).")
            if (mettre_l == ""):
                  #did not do 5$ part yet
                  if (litre_en_mettant_le_gas < litre_dans_le_reservoir_total) and (litre_en_mettant_le_gas > litre_dans_le_reservoir_total - 1):
                        mettre_moins_de_1l = mettre_moins_de_1l + 1
                        print("mettre_moins_de_1l", mettre_moins_de_1l)
                        final_l = litre_dans_le_reservoir_total - litre_en_mettant_le_gas

                        if (essence_type == "O"):
                              final_liter_price = final_l * prix_essence_ordinaire
                              prix_gas = prix_gas + final_liter_price
                              litre_en_mettant_le_gas = litre_en_mettant_le_gas + final_l
                              print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",
                                    litre_dans_le_reservoir_total, "\n"
                                                                   "Coût (jusqu'à maintenant) : ", prix_gas, "$")
                        else:
                              if (essence_type == "D"):
                                    final_liter_price = final_l * prix_essence_diesel
                                    prix_gas = prix_gas + final_liter_price
                                    litre_en_mettant_le_gas = litre_en_mettant_le_gas + final_l
                                    print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",
                                          litre_dans_le_reservoir_total, "\n"
                                                                         "Coût (jusqu'à maintenant) : ", prix_gas, "$")
                              else:
                                    if (essence_type == "S"):
                                          final_liter_price = final_l * prix_essence_super
                                          prix_gas = prix_gas + final_liter_price
                                          litre_en_mettant_le_gas = litre_en_mettant_le_gas + final_l
                                          print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",
                                                litre_dans_le_reservoir_total, "\n"
                                                                               "Coût (jusqu'à maintenant) : ", prix_gas,
                                                "$")
                  #not done
                  if (litre_en_mettant_le_gas + 1 <= litre_dans_le_reservoir_total):
                        if (total_prix_desirer >= prix_gas):
                              litre_en_mettant_le_gas = litre_en_mettant_le_gas + 1
                              if (essence_type == "O"):
                                    prix_gas = prix_gas + prix_essence_ordinaire
                                    print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",
                                          litre_dans_le_reservoir_total, "\n""Coût (jusqu'à maintenant) : ", prix_gas, "$")
                              else:
                                    if (essence_type == "D"):
                                          prix_gas = prix_gas + prix_essence_diesel
                                          print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",
                                                litre_dans_le_reservoir_total, "\n"
                                                                               "Coût (jusqu'à maintenant) : ", prix_gas, "$")
                                    else:
                                          if (essence_type == "S"):
                                                prix_gas = prix_gas + prix_essence_super
                                                print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",
                                                      litre_dans_le_reservoir_total, "\n"
                                                                                     "Coût (jusqu'à maintenant) : ", prix_gas,"$")
                        else:
                              mettre_essence = False


                  if (litre_en_mettant_le_gas >= litre_dans_le_reservoir_total):
                        mettre_essence = False
            if (mettre_l == "A"):
                  mettre_essence = False

print("bitchass")


if (mettre_l == "A"):
      print("terminé!")
      print("stop")
else:
      print("Cela est un choix invalid! Veuillez essayer encore S.V.P!")




#Remplissage litre par litre
#Entrer un code promotionnel
#Affichage final


if (plein_ou_fixe == "M"):
      total_prix_desirer = float(input("Veuillez inscrire le montant souhaité : "))
      mettre_l = input("Appuyez sur entrée pour ajounter un litre (A pour arrêter).")

      if (mettre_l == ""):
            if (litre_dans_le_reservoir_total - litre_en_mettant_le_gas) / 1 <= (
                    total_prix_desirer - prix_gas) / prix_essence:
                  prix_en_premier = False
            if prix_en_premier == False:
                  # when gas will fill first
                  if (litre_en_mettant_le_gas < litre_dans_le_reservoir_total) and (
                          litre_en_mettant_le_gas > litre_dans_le_reservoir_total - 1):
                        final_l = litre_dans_le_reservoir_total - litre_en_mettant_le_gas
                        prix_gas = prix_gas + prix_essence
                        litre_en_mettant_le_gas = litre_en_mettant_le_gas + final_l
                        print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",
                              litre_dans_le_reservoir_total, "\n"
                                                             "Coût (jusqu'à maintenant) : ", round(prix_gas, 2), "$")

                  # il rest moin que un litre de place
                  if (litre_en_mettant_le_gas + 1 <= litre_dans_le_reservoir_total):
                        litre_en_mettant_le_gas = litre_en_mettant_le_gas + 1
                        prix_gas = prix_gas + prix_essence
                        print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",
                              litre_dans_le_reservoir_total, "\n"
                                                             "Coût (jusqu'à maintenant) : ", round(prix_gas, 2), "$")

                  if (litre_en_mettant_le_gas >= litre_dans_le_reservoir_total):
                        mettre_essence = False
            if prix_en_premier == True:
                  # when money limit will fill up first
                  if (prix_gas + prix_essence <= total_prix_desirer):
                  # do a full liter
                  if (prix_gas + prix_essence > total_prix_desirer):
            # how much money is left by substracting by our max

      if (mettre_l == "A"):
            mettre_essence = False
