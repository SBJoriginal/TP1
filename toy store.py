cash = 0
Numero = False
while not Numero:
    try:
        cash = int(
            input("Bienvenue au monde de jouet. Veuillez inscrire combien d'argent vous avez avant de commencer: "))
        Numero = True
    except ValueError:
        print("Cela n'est pas un numéro! SVP entrer un numéro.")
print("Merci!")
cash_spent = cash
fini = "N"
while fini == "N":
    print("il vous reste", cash, "$")
    will_you_buy_one = input(
        "Si vous voulez acheter un jouet pour 1$, pesez n'importe quelle touche et ENTER, sinon écrivez 'stop' et puis pesez la touche ENTER: ")
    while will_you_buy_one != "stop":
        if (int(cash) <= 0):
            print("Désoler! Vous n'avez plus d'argent")
            will_you_buy_one = "stop"
            fini = "Y"
            break
        cash = int(cash) - 1
        Montant_depense = (int(cash_spent) - int(cash))
        print("il vous reste", cash, "$")
        print("Vous avez dépensé", Montant_depense, "$")
        will_you_buy_one = input(
            "Si vous voulez acheter un jouet pour 1$, pesez n'importe quelle touche et ENTER, sinon écrivez 'stop' et puis pesez la touche ENTER: ")
        if (cash <= 0):
            print("Désoler! Vous n'avez plus d'argent")
            will_you_buy_one = "stop"
            fini = "Y"

    if (fini != "Y"):
        fini = input("Voulez-vous arrêter de magasiner? Répondre en utilisant Y ou N respectivement: ")
        while fini not in ["Y", "N"]:
            print("Cela est une touche invalide.")
            fini = input("Voulez-vous arrêter de magasiner? Répondre en utilisant Y ou N respectivement: ")
fini = "N"
Montant_depense = (int(cash_spent) - int(cash))
print("Vous avez dépensé", Montant_depense, "$ au total pour", Montant_depense, "jouet!")
print("Il vous reste maintenant", cash, "$")
print("Merci beaucoup et bonne journée")
