
a = 2
b = 3
c = 5
d = 9
a = b + c
b = a - (c * 2)
c = c * b
a, b = b, a
a = -a
d = b // c
print( a, b, c, d)

r, pi = 12, 3.14159
s = pi * r**2 #pi x (r ^ 2)
print(s)

#2.1-2.2-2.3
annee = 2022
nom = input("Quel est votre nom? ")
naissance = int(input("Quelle est votre date de naissance? "))
age = annee - naissance
print("Bonjour,", nom)
print("Vous avez",age , "ans")
variable = False
while not variable:
    try:
        a_1 = int(input("Enter a first number: "))
        a_2 = int(input("Enter a second number: "))
        variable = True
    except ValueError:
        print("that is not a number! Please try again")
a_3 = a_1 + a_2
print("The total of these two numbers is:", a_3)

#nombre premier
nombre = int(input("Entrez un nombre: "))
somme = 0
while nombre != 0:
    somme = somme + nombre
    nombre = int(input("Entrez un autre nombre: "))
print("la somme est de", somme)

#3.2
annee_entrer = int(input("Entrez une annee :"))
if annee_entrer % 4 == 0:
    if annee_entrer % 100 == 0:
        if annee_entrer % 400 == 0:
            print("C'est une annee bissextile")
        else:
            print("Ce n'est pas une annee bissextile")
    else:
        print("C'est une annee bissextile")
else:
    print("Ce n'est pas une annee bissextile")

#nombre premier
chiffre = int(input("Entrez un nombre: "))
est_premier = True
if (chiffre == 0) or (chiffre == 1) :
    est_premier = False
else:
    for diviseur_potentiel in range(2, chiffre//2 +1):
        if chiffre % diviseur_potentiel == 0:
            est_premier = False
if (est_premier == True):
    print("le chiffre est un nombre premier")
else:
    print("le chiffre n'est pas un nombre premier")




