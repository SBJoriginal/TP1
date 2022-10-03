#
#Salut! Ceci est mon premier vrai code! Je suis sure qu'il pourrait être beaucoup mieux, mais je suis très fier! J'ai decidé de ne pas donner des valeurs aléatoires au gas et aux autos, car j'ai passé beaucoup de temps à trouver une manière de m'assurer que les valuers entrés maunellements soient forcements un float positif peut importe la situation. Je me suis dit qu'en mettant un randomiser je perdais beaucoup de ce code et temps!
#Configuration de la pompe à essence
#pour etre sur que le prix d'essence est un float positif
print("Coniguration de la pompe à essence...")
negative_number = True
gas_float = False

while negative_number == True or gas_float == False:
    prix_essence_ordinaire = (input("Quel est le prix de l’essence ordinaire en ($/L) : "))
    prix_essence_diesel = (input("Quel est le prix de l’essence diesel en ($/L) : "))
    if prix_essence_ordinaire.replace(".", "", 1).isdigit() and prix_essence_diesel.replace(".", "", 1).isdigit():
        gas_float = True
        prix_essence_ordinaire = float(prix_essence_ordinaire)
        prix_essence_diesel = float(prix_essence_diesel)
        if (prix_essence_ordinaire < 0) or (prix_essence_diesel < 0):
            print("Cela est un choix invalid! Veuillez essayer encore S.V.P.!")
        else:
            negative_number = False
    else:
        print("Cela est un choix invalid! Assurez-vous d'utiliser un [.] et non un [,] pour les nombres décimaux. Veuillez essayer encore S.V.P.!")
#les donnees pour le TP
car_never_stop_coming = True
prix_essence_super = (prix_essence_ordinaire * 1.1)
code_secret_du_jour = input("Quel est le code secret du jour : ")
while car_never_stop_coming == True:
      choix_dessence = False
      choix_plein_ou_fixe = False
      mettre_essence = True
      prix_en_premier = True
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

      print("∗∗∗∗∗∗∗∗∗∗\n"
            "une automobile arrive.")
      #Arrivée d’une automobile(impossible d'avoir un input autre que float positif et des cas impossible comme le reservoir est plus plein ou egal que le maximum
      negative_number_litre = True
      litre_float = False
      capacite_impossible = True

      while negative_number_litre == True or litre_float == False or capacite_impossible == True:
            negative_number_litre = True
            litre_float = False
            capacite_impossible = True
            litre_dans_le_reservoir_total = input("La nombre de litres total de ton réservoir est ")
            litre_dans_le_reservoir_avant = input("et il en contient actuellement ")
            if litre_dans_le_reservoir_total.replace(".", "", 1).isnumeric() and litre_dans_le_reservoir_avant.replace(
                    ".", "", 1).isnumeric():
                  litre_float = True
                  litre_dans_le_reservoir_total = float(litre_dans_le_reservoir_total)
                  litre_dans_le_reservoir_avant = float(litre_dans_le_reservoir_avant)
                  if (litre_dans_le_reservoir_total < 0) or (litre_dans_le_reservoir_avant < 0):
                        print("Cela est un choix invalid! Veuillez essayer encore S.V.P!")
                  else:
                        negative_number_litre = False
                        while capacite_impossible == True:
                              if litre_dans_le_reservoir_total <= litre_dans_le_reservoir_avant:
                                    print("votre capacité d'essence est déjà au maximum! Veuillez essayer encore S.V.P!")
                                    negative_number_litre = True
                                    litre_float = False
                                    capacite_impossible = False
                              else:
                                    capacite_impossible = False
            else:
                  print("Cela est un choix invalid! Assurez-vous d'utiliser un [.] et non un [,] pour les nombres décimaux. Veuillez essayer encore S.V.P!")

      #Demander le type d’essence
      print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
            "- - -                                 Affichage sur la pompe                                             - - -\n"
            "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
            "Veuillez sélectionner le type d'essence parmi : \n"
            "-  [O] rdinaire : ",prix_essence_ordinaire, "$ / litre \n"
            "-  [S] uper : ",round(prix_essence_super, 2), "$ / litre \n"
            "-  [D] iesel : ",prix_essence_diesel, "$ / litre ")

#pour le prix d"essence
      while choix_dessence == False:
            essence_type = input("Votre choix (O, S ou D) : ")
            if essence_type.lower() == "o":
                  choix_dessence = True
                  prix_essence = prix_essence_ordinaire
            else:
                  if (essence_type.lower() == "s"):
                        choix_dessence = True
                        prix_essence = prix_essence_super
                  else:
                        if (essence_type.lower() == "d"):
                              choix_dessence = True
                              prix_essence = prix_essence_diesel
                        else:
                              print("Cela est un choix invalide! Veuillez essayer encore S.V.P.!")

      #Demander le plein ou un montant fixe (le montant fixe doit etre un float positif)
      while choix_plein_ou_fixe == False:
            plein_ou_fixe = input("Souhaitez-vous faire le plein (P) ou choisir un montant fixe (M) ? ")
            if (plein_ou_fixe.lower() == "p"):
                  choix_plein_ou_fixe = True
            else:
                  if (plein_ou_fixe.lower() == "m"):
                        negative_fixe = True
                        fixe_float = False
                        while negative_fixe == True or fixe_float == False:
                              total_prix_desirer = input("Veuillez inscrire le montant souhaité : ")
                              if total_prix_desirer.replace(".", "", 1).isdigit():
                                    fixe_float = True
                                    total_prix_desirer = float(total_prix_desirer)
                                    if (total_prix_desirer < 0):
                                          print("Cela est un choix invalide! Veuillez essayer encore S.V.P.!")
                                    else:
                                          negative_fixe = False
                              else:
                                    print("Cela est un choix invalide! Veuillez essayer encore S.V.P.!")

                        choix_plein_ou_fixe = True
                  else:
                        print("Cela est un choix invalide! Assurez-vous d'utiliser un [.] et non un [,] pour les nombres décimaux. Veuillez essayer encore S.V.P.!")

      #Remplissage litre par litre
      print("Remplissage!")
      litre_en_mettant_le_gas = litre_dans_le_reservoir_avant

      while mettre_essence == True:
            #si l'tutilisateur choix le plein
            if (plein_ou_fixe.lower() == "p"):
                  mettre_l = input("Appuyez sur entrée pour ajounter un litre (A pour arrêter).")
                  if (mettre_l == ""):
                        # il reste moins que un litre de place
                        if (litre_en_mettant_le_gas + 1 > litre_dans_le_reservoir_total):
                              final_l = litre_dans_le_reservoir_total - litre_en_mettant_le_gas
                              litre_en_mettant_le_gas = litre_en_mettant_le_gas + final_l
                              prix_gas = prix_gas + (prix_essence * final_l)
                              print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur",litre_dans_le_reservoir_total, "\n"
                                    "Coût (jusqu'à maintenant) : ", round(prix_gas, 2), "$")
                        #il reste au moins 1 litre
                        if (litre_en_mettant_le_gas <= litre_dans_le_reservoir_total - 1):
                              litre_en_mettant_le_gas = litre_en_mettant_le_gas + 1
                              prix_gas = prix_gas + prix_essence
                              litre_en_mettant_le_gas = litre_en_mettant_le_gas
                              print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur", litre_dans_le_reservoir_total,"\n"
                                    "Coût (jusqu'à maintenant) : ", round(prix_gas, 2), "$")
                        #il reste plus de place
                        if (litre_en_mettant_le_gas >= litre_dans_le_reservoir_total):
                              mettre_essence = False
                  if (mettre_l.lower() == "a"):
                        mettre_essence = False
                        print("État du réservoir d'essence : ", litre_en_mettant_le_gas, "sur", litre_dans_le_reservoir_total,"\n"
                              "Coût (jusqu'à maintenant) : ", round(prix_gas, 2), "$")

            # si l'tutilisateur choix un montant fixe
            if (plein_ou_fixe.lower() == "m"):
                  #ceci est pour savoir si le plein de litre ou du montant fixe va remplir en premier
                  if (litre_dans_le_reservoir_total - litre_en_mettant_le_gas) / 1 < (total_prix_desirer - prix_gas) / prix_essence:
                        prix_en_premier = False
                  else:
                        prix_en_premier = True

                  mettre_l = input("Appuyez sur entrée pour ajounter un litre (A pour arrêter).")
                  if (mettre_l == ""):
                        #le reservoir d'essence va se remplir en premier
                        if prix_en_premier == False:
                              # il reste moins que un litre de place
                              if (litre_en_mettant_le_gas + 1 > litre_dans_le_reservoir_total):
                                    final_l = litre_dans_le_reservoir_total - litre_en_mettant_le_gas
                                    litre_en_mettant_le_gas = litre_en_mettant_le_gas + final_l
                                    prix_gas = prix_gas + (prix_essence * final_l)
                                    print("État du réservoir d'essence : ", round(litre_en_mettant_le_gas, 2), "sur",litre_dans_le_reservoir_total, "\n"
                                          "Coût (jusqu'à maintenant) : ", round(prix_gas, 2),"$")

                              # il reste au moins 1 litre
                              if (litre_en_mettant_le_gas <= litre_dans_le_reservoir_total - 1):
                                    litre_en_mettant_le_gas = litre_en_mettant_le_gas + 1
                                    prix_gas = prix_gas + prix_essence
                                    litre_en_mettant_le_gas = litre_en_mettant_le_gas
                                    print("État du réservoir d'essence : ", round(litre_en_mettant_le_gas, 2), "sur",litre_dans_le_reservoir_total, "\n"
                                          "Coût (jusqu'à maintenant) : ", round(prix_gas, 2),"$")

                              # il reste plus de place
                              if litre_en_mettant_le_gas >= litre_dans_le_reservoir_total:
                                    mettre_essence = False
                                    prix_en_premier = 0



                       #le montant fixe d'argent va remplir en premier
                        if prix_en_premier == True:

                              # il reste moins que un litre de place
                              if (prix_gas + prix_essence > total_prix_desirer):
                                    final_dollar = total_prix_desirer - prix_gas
                                    prix_gas = prix_gas + final_dollar
                                    litre_en_mettant_le_gas = (final_dollar / prix_essence) + litre_en_mettant_le_gas
                                    print("État du réservoir d'essence : ", round(litre_en_mettant_le_gas, 2), "sur",litre_dans_le_reservoir_total, "\n"
                                          "Coût (jusqu'à maintenant) : ", round(prix_gas, 2),"$")


                              # il reste au moins 1 litre
                              if (prix_gas + prix_essence <= total_prix_desirer):
                                    litre_en_mettant_le_gas = litre_en_mettant_le_gas + 1
                                    prix_gas = prix_gas + prix_essence
                                    print("État du réservoir d'essence : ", round(litre_en_mettant_le_gas, 2), "sur",litre_dans_le_reservoir_total, "\n"
                                          "Coût (jusqu'à maintenant) : ", round(prix_gas, 2),"$")

                              # il reste plus de place
                              if (prix_gas >= total_prix_desirer):
                                    mettre_essence = False
                                    prix_en_premier = 0

                  if mettre_l.lower() == "a":
                        mettre_essence = False

      #Entrer un code promotionnel
      print("Terminé!\n"
            "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
      code_secret_entrez = input("Si vous connaissez le code promotionnel RABAIS+, entrez - le maintenant pour \n"
                                 "obtenir 30% de rabais: ")
      if code_secret_entrez == code_secret_du_jour:
            print("Code valide.")
            prix_gas = 0.7 * prix_gas
      else:
            print("Code non valide.")

      #Affichage final
      print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
             "Le montant final est :", round(prix_gas, 2), "$\n"
            "Faites bonne route !")
