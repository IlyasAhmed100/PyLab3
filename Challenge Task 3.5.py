# Challenge Task 3.5

# Entering the size of the box
size = int(input("Please enter the width of the box: "))

# Work out size of box
print("*" * size)
for i in range (size - 2):
    print("*" + " " * (size - 2) + "*")
print("*" * size)


