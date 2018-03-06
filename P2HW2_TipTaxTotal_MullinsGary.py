# CTI-110 
# Tip Tax Total 
# Gary Mullins
# 02/27/2018

# constant for the tax and tip rate.
Tip_Rate=0.07
Tax_Rate=0.18

# Declare variable for the food charges,tip,tax and the total.
foodcost=0.0
tax=0.0
tip=0.0
total=0.0

# Get the foodcost.
foodcost = float(input("Enter the food cost"))

# Calculate the tip.
tip = foodcost* Tip_Rate

# Calculate the tax.
tax = foodcost*Tax_Rate
# calculate the total.
total = foodcost + tip + tax

# Print the tip,tax,total.
print("Tip: $ ",format(tip, '.2f'))
print("tax: $",format(tax, '.2f'))
print("total: $",format(total, '.2f'))
