# Michael Kodel
# 9/6/2026
# P1HW2
# This program will take user input for a travel destination and budget and print out a travel plan based on the input

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter your budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
accommodation = int(input("How much do you think you will spend on accommodation/hotel? "))
print()
food = int(input("How much do you think you will spend on food? "))
print()

print("----------Travel Expenses----------")
print("Location: " + destination)
print("Initial Budget: $" + str(budget))
print()
print("Fuel: $" + str(gas))
print("Accommodation: $" + str(accommodation))
print("Food: $" + str(food))
print()
print("Remaining Balance: $" + str(budget - (gas + accommodation + food)))

