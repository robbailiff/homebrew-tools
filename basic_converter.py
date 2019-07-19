print("""
Homebrew Recipe Converter Tool
==============================

This is a basic tool designed to convert the value ingredient in a brewing recipe at a specified batch size, to the batch size you plan to make.

""")

user_item = input("Enter the name of the item you want to convert: ")
item_weight = float(input("Enter the weight (in g) of the item: "))
recipe_vol = float(input("Enter the batch volume (in l) of the original recipe: "))
desired_vol = float(input("Enter the desired volume (in l) you want to end up with: "))

converted_weight = round((item_weight / recipe_vol * desired_vol), 2)

print(" ")
print("You require {}g of {} for a {}l recipe".format(converted_weight, user_item, desired_vol))
