getal1 = float(input("Eerste getal:  "))
getal2 = float(input("Tweede getal:  "))

#check welke de grootste is
if getal1>getal2:
    print(getal1-getal2)
elif getal2>getal1:
    print(getal2-getal1)
else:
    print("De twee getallen zijn hetzelfde")