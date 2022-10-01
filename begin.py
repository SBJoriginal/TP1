

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




print("out")