

negative_number_litre = True
litre_float = False
capacite_impossible = True

while negative_number_litre == True or litre_float == False or capacite_impossible == True:
    negative_number_litre = True
    litre_float = False
    capacite_impossible = True
    litre_dans_le_reservoir_total = input("La nombre de litres total de ton réservoir est ")
    litre_dans_le_reservoir_avant = input("et il en contient actuellement ")
    if litre_dans_le_reservoir_total.replace(".", "", 1).isnumeric() and litre_dans_le_reservoir_avant.replace(".", "", 1).isnumeric():
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
        print("Cela est un choix invalid! Veuillez essayer encore S.V.P!")

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
        print("Cela est un choix invalid! Veuillez essayer encore S.V.P.!")




print("out")