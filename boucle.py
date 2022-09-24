x = int(input("entrez un numbre x: "))
n = int(input("Entrez un numbre n: "))

resultat = 1
i = 0

while i < n:
    resultat = resultat * x
    i = i + 1
print ("x exposant n vaut", resultat)