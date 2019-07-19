print("""
Homebrew ABV Addition Tool
==========================

This tool is designed to calculate the final abv of a homebrew after adding other alcohol to it (e.g. adding whisky to porter to create a bourbon porter)

""")

abv1 = float(input("Enter the ABV (%) of the first item: "))
print(str(abv1) + "%")
volume1 = float(input("Enter the volume (ml) of the first item: "))
print(str(volume1) + "ml")

abv2 = float(input("Enter the ABV (%) of the second item: "))
print(str(abv2) + "%")
volume2 = float(input("Enter the volume (ml) of the second item: "))
print(str(volume2) + "ml")

weight1 = ((abv1/100) * volume1)
weight2 = ((abv2/100) * volume2)

print(weight1)
print(weight2)

total_abv = ((weight1 + weight2) / (volume1 + volume2)) * 100
print(" ")
print(str(total_abv) + "%")
