# Task 3.2

# Asks user to input two numbers to add together
print("We are going to add two numbers together")
sum_1 = int(input("Please enter your first number: "))
sum_2 = int(input ("Please enter your second number: "))
# Should add two numbers together
sum_total = sum_1 + sum_2
print(sum_total)

# Asks user to input two numbers to subtract from each other
print("We are going to subtract two numbers from each other")
dif_1 = int(input("Please enter your first number: "))
dif_2 = int(input("Please enter your second number: "))
# Should subtract two numbers from each other
dif_total = dif_1 - dif_2
print(dif_total)

# Asks user to input two numbers to multiply together
print("We are going to multiply two numbers together")
mult_1 = int(input("Please enter your first number: "))
mult_2 = int(input("Please enter your second number: "))
# Should multiply two numbers togehter
mult_total = mult_1 * mult_2
print(mult_total)

# Asks user to input two numbers to work out the average
print("We are going to work out the average of two numbers")
avr_1 = float(input("Please enter your first number: "))
avr_2 = float(input("Please enter your second number: "))
# Should work out the average of the two numbers
avr_add = avr_1 + avr_2
avr_total = avr_add / 2
print(avr_total)

# Asks user to input two numbers to work out the distance between them
print("We are going to work out the absolute value of the difference between two numbers")
abs_1 = int(input("Please enter your first number: "))
abs_2 = int(input("Please enter your second number: "))
# Should work out the absolute value between the two numbers
abs_total = abs_1 - abs_2
abs_value = abs(abs_total)
print(abs_value)

# Asks user to input two numbers to work out the larger one
print("We are going to work out which of the two numbers is bigger")
size_1 = int(input("Please enter your first number: "))
size_2 = int(input("Please enter your second number: "))
# Should work out the larger number
if size_1 > size_2:
    print(size_1)
else:
    print(size_2)

# Asks user to input two numbers to work out the smaller one
print("We are going to work out which of the two numbers is smaller")
size_3 = int(input("Please enter your first number: "))
size_4 = int(input("Please enter your second number: "))
# Should work out the smaller number
if size_3 < size_4:
    print(size_3)
else:
    print(size_4)
