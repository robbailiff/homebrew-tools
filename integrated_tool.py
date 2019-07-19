"""
Integrated Homebrew Recipe Converter Tool
=========================================

This tool is designed to take a beer recipe for a certain batch size, convert it to a new batch size, do the water volume calculations, and display it as a recipe
in bullet point form. It is meant mainly as a handy reference on brew day. Since I plan on using this myself, for simplicity I have made all of the units in grams
and litres, and have kept some of the numbers (e.g. evaporation rate) constant based on my own system. 

For anyone wanting to try out the code, I have included a 100 character example recipe here, and a longer recipe at the bottom of the script 
(copy from below here):

My Beer
20
10
Yes
Pale Malt
5000
No
Yes
Goldings
45
60
No
Yes
Yeast
10
g
At start
7 days
No

"""

# Start of the script
recipe_name = input("Enter the name of your recipe: ")
recipe_vol = float(input("Enter the batch volume (in l) of the original recipe: "))
desired_vol = float(input("Enter the desired volume (in l) you want to end up with: "))

# Empty dictionaries
mash_dict = {}
boil_dict = {}
fermenter_dict = {}

# Loop for mash ingredients
while True:

    print("Would you like to add an ingredient to the mash?")
    user_input = input("Enter 'Yes' or 'No': ")
    print(" ")

    if user_input == "No" or user_input == "no":
        break
    elif user_input == "Yes" or user_input == "yes":
        mash_item = input("Enter the name of the item you want to add to the mash: ")
        mash_weight = float(input("Enter the original recipe weight (in g) of the item: "))
        converted_weight = round((mash_weight / recipe_vol * desired_vol), 2)
        mash_dict[mash_item] = converted_weight
    else:
        print("User input was not valid.\n")
        continue

# Loop for boil ingredients
while True:

    print("Would you like to add an ingredient to the boil?")
    user_input = input("Enter 'Yes' or 'No': ")
    print(" ")

    if user_input == "No" or user_input == "no":
        break
    elif user_input == "Yes" or user_input == "yes":
        boil_item = input("Enter the name of the item you want to add to the boil: ")
        boil_weight = float(input("Enter the original recipe weight (in g) of the item: "))
        boil_time = int(input("Enter the boil time (in mins) for this item: "))
        converted_weight = round((boil_weight / recipe_vol * desired_vol), 2)
        boil_dict[boil_item] = [converted_weight, boil_time]
    else:
        print("User input was not valid.\n")
        continue

# Loop for fermenter ingredients
while True:

    print("Would you like to add an ingredient to the fermenter?")
    user_input = input("Enter 'Yes' or 'No': ")
    print(" ")

    if user_input == "No" or user_input == "no":
        break
    elif user_input == "Yes" or user_input == "yes":
        fermenter_item = input("Enter the name of the item you want to add to the fermenter: ")
        fermenter_weight = float(input("Enter the original recipe weight (in g) or volume (in l) of the item: "))
        fermenter_units = input("Enter the units the item is measured in: ")
        fermenter_time = input("Enter when you add this item: ")
        fermenter_length = input("Enter how long this item should be in the fermenter: ")
        converted_weight = round((fermenter_weight / recipe_vol * desired_vol), 2)
        fermenter_dict[fermenter_item] = [converted_weight, fermenter_time, fermenter_length, fermenter_units]
    else:
        print("User input was not valid.\n")
        continue

# Function to iterate through mash dictionary
def mash():
    if len(mash_dict) != 0:

        print("""
        Mash Ingredients
        ================
        """)

        for key, value in mash_dict.items():
            name = key
            weight = value

            print(f"\t* {key.capitalize()} = {weight}g")

# Function to iterate through boil dictionary
def boil():
    if len(boil_dict) != 0:

        print("""
        Boil Ingredients
        ================
        """)

        for key, value in boil_dict.items():
            name = key
            weight = value[0]
            time = value[1]

            print(f"\t* {key.capitalize()} = {weight}g (Add {time} mins before the end of the boil)")

# Function to iterate through fermenter dictionary
def fermenter():
    if len(fermenter_dict) != 0:

        print("""
        Fermenter Ingredients
        =====================
        """)

        for key, value in fermenter_dict.items():
            name = key
            weight = value[0]
            time = value[1]
            length = value[2]
            unit = value[3]

            print(f"\t* {key.capitalize()} = {weight}{unit} (Add {time} and leave in the fermenter {length})")

# Function to display water calculations
def water_vol():

    print(f"""
    \tWater Volume
    \t============
    """)

    grain_weight = sum(mash_dict.values())

    mash_vol = round(((grain_weight/1000) * 3), 2)
    grain_abs = round((grain_weight/1000), 2) # 1kg of grain absorbs 1 litre of mash water so it's effectively the same value as grain_weight
    first_run = round((mash_vol - grain_abs), 2)

    trub_loss = 1 # Could add a user input for this value later
    fermenter_vol = round((desired_vol + trub_loss), 2)
    kettle_loss = 0 # Could add a user input for this value later
    post_boil_vol = round((fermenter_vol + kettle_loss), 2)


    evap_rate = 2.5 # Could add a user input for this value later
    pre_boil_vol = round((post_boil_vol + evap_rate), 2)
    sparge_vol = round((pre_boil_vol - first_run), 2)

    print("\tMash Volume = {} l".format(mash_vol))
    print("\tFirst Runnings Volume = {} l".format(first_run))
    print("\tSparge Volume = {} l".format(sparge_vol))
    print("\tPre-boil Volume = {} l".format(pre_boil_vol))
    print("\tPost-boil Volume = {} l".format(post_boil_vol))


underline = "=" * (len(recipe_name) + 7)

# Below here is where the recipe will print out
print(f"""
{recipe_name} Recipe
{underline}
{underline}
""")

mash()
boil()
fermenter()
water_vol()

print("""
Enjoy your homebrew!
""")

# End of script

"""
Example recipe (copy from below here):

Vanilla Porter
20
10
Yes
Pale Malt
5000
Yes
Munich Malt
650
Yes
Crystal Malt
450
Yes
Chocolate Malt
350
Yes
Black Malt
200
No
Yes
Kent Goldings
45
60
No
Yes
Yeast
10
g
At start
7 days
Yes
Vanilla Pod
10
g
At the start of fermentation
7 days
No

"""
