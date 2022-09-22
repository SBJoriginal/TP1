Numero = False

while not Numero:
    try:
        cash = int(input("Bienvenue au monde de jouet. Veuiller inscrire combien d'argent vous-avez avant de commencer: "))
        Numero = True
    except ValueError:
        print("That isn't a number! Please try again")
print("Thank you")