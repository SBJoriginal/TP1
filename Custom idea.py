#cash register.
#menu of items with various prices
#you get to choose the items
#go to cart and checkout
#cc information
#buy

continue_shopping = True
cart_total_price = 0
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
a = "Apple"
b = "Banana"
c = "Chips"
d = "Dumplings"
e = "Egg"
f = "Fries"
Aa = 1.50
Bb = 2.50
Cc = 4.75
Dd = 7.15
Ee = 2.30
Ff = 5.85

if continue_shopping == True:
      print("Welcome to MELIMELO groce54ory store! \n"
            "Select any of the items by inputing the letters corresponding to the item. \n"
            "You can type cart at any time to check what items you have selected \n"
            "(A) Apple.........1.50$\n"
            "(B) Banana........2.50$\n"
            "(C) Chips.........4.75$\n"
            "(D) Dumplings.....7.15$\n"
            "(E) Egg...........2.30$\n"
            "(F) Fries.........5.85$\n"
            "(cart) View your cart")
while continue_shopping == True:
      while continue_shopping == True:
            product = input("Entrez la lettre du produit dont vous voulez: ")
            if (product == "A"):
                  A = A + 1
                  print("A")
                  print("A", A)
            else:
                  if (product == "B"):
                        B = B + 1
                        print("B")
                        print("B", B)
                  else:
                        if (product == "C"):
                              C = C + 1
                              print("C")
                              print("C", C)
                        else:
                              if (product == "D"):
                                    D = D + 1
                                    print("D")
                                    print("D", D)
                              else:
                                    if (product == "E"):
                                          E = E + 1
                                          print("E")
                                          print("E", E)
                                    else:
                                          if (product == "F"):
                                                F = F + 1
                                                print("F")
                                                print("F", F)
                                          else:
                                                if (product == "cart"):
                                                      print("going to cart")
                                                      continue_shopping = False
                                                else:
                                                      print("That is not a valid entry! Please try again")
      cart_total_price = A * Aa + B * Bb + C * Cc + D * Dd + E * F * Ff
      print("Your cart is as follows: ")
      if A > 0:
            print("You have a chosen", A, a)
      if B > 0:
            print("You have a chosen", B, b)
      if C > 0:
            print("You have a chosen", C, c)
      if D > 0:
            print("You have a chosen", D, d)
      if E > 0:
            print("You have a chosen", E, e)
      if F > 0:
            print("You have a chosen", F, f)
      print("Your current total is", cart_total_price, "$")
      #add the total of the prices
      continue_shopping = input("Do you want to keep shopping (yes or no): ")
      if continue_shopping == "yes":
            continue_shopping = True
print("thank you for shopping wiht us\n"
      "Your total is", cart_total_price)



