verbruik = float(input("verbruik per 100km:   "))
prijs = float(input("prijs per liter:      "))

vijf = (verbruik/20)*prijs
vijftwintig = (verbruik/4)*prijs
honderd = verbruik*prijs

print("5km = €", vijf)
print("25km = €", vijftwintig)
print("100km = €", honderd)