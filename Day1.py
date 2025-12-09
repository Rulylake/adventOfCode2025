import math as ma

file = open("Day1Input")
instructions = file.read().split("\n")

currValue = 50
password1 = 0
password2 = 0
for instruction in instructions:
    direction = instruction[0]
    amount = int(instruction[1:])

    while amount > 99:
        amount -= 100
        password2 += 1

    if direction == "R":
        if currValue + amount > 99:
            password2 += 1
        currValue += amount
    else:
        if currValue - amount <= 0 and currValue != 0:
            password2 += 1
        currValue -= amount
        

    while currValue < 0:
        currValue += 100
    
    while currValue > 99:
        currValue -= 100

    if currValue == 0:
        password1 += 1

print("password1: " + str(password1))
print("password2: " + str(password2))