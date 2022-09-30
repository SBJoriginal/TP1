
negative_number = True
gas_float = False



while negative_number == True or gas_float == False:
    prix_essence_ordinaire = (input("Quel est le prix de l’essence ordinaire en ($/L) : "))
    prix_essence_diesel = (input("Quel est le prix de l’essence diesel en ($/L) : "))
    if prix_essence_ordinaire.isdigit() or prix_essence_ordinaire:
        print("C")
        gas_float = True
        prix_essence_ordinaire = float(prix_essence_ordinaire)
        prix_essence_diesel = float(prix_essence_diesel)
        if (prix_essence_ordinaire < 0) or (prix_essence_diesel < 0):
            print("B")
        else:
            negative_number = False
    else:
        print("A")




print("out")