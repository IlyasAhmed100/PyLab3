# Task 3.3

# Asks the user to print the price of the drink and number of drinks bought
price_of_drink = float(input("Please enter the price of your drink: "))
number_of_drinks_bought = int(input("Please enter the number of drinks bought: "))

# Works out the total costs of drinks to two decimal places
total_price_of_drinks = price_of_drink * number_of_drinks_bought
print("£" + "%.2f" % total_price_of_drinks)
                       
