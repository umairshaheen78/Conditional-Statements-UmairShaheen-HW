# Prompt the user for the amount of cents and store it in a variable 
c=int(input('Please enter an amount of cents:'))

# Conditional Statements to calculate the number of each type of coin

# Quarters: 25c
# Dimes: 10c
# Nickels: 5c
# Pennies: 1c
'''--------------------------------'''
print(c//25, "quarters")
c = c%25
print(c//10, "dimes")
c = c%10
print(c//5, "nickles")
c = c%5
print(c//1, "pennies")