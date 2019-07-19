print("""
Homebrew Water Volume Calculator
================================

This is a tool for calculating water volumes for homebrewing based on a specified batch size. All the units are in grams and litres.

""")

grain_weight = float(input("Enter the total weight (in g) of the grain for this recipe: "))
batch_size = float(input("Enter the desired volume (in l) for this recipe: "))

mash_vol = round(((grain_weight/1000) * 3), 2)
grain_abs = round((grain_weight/1000), 2) # 1kg of grain absorbs 1 litre of mash water so it's effectively the same value as grain_weight
first_run = round((mash_vol - grain_abs), 2)


trub_loss = 1 # Could add a user input for this value later
fermenter_vol = round((batch_size + trub_loss), 2)
kettle_loss = 0 # Could add a user input for this value later
post_boil_vol = round((fermenter_vol + kettle_loss), 2)


evap_rate = 2.5 # Could add a user input for this value later
pre_boil_vol = round((post_boil_vol + evap_rate), 2)
sparge_vol = round((pre_boil_vol - first_run), 2)

print(" ")
print("Your mash volume is {} litres.".format(mash_vol))
print("Your first runnings volume is {} litres.".format(first_run))
print("Your sparge volume is {} litres.".format(sparge_vol))
print("Your pre-boil volume is {} litres.".format(pre_boil_vol))
print("Your post-boil volume is {} litres.".format(post_boil_vol))
