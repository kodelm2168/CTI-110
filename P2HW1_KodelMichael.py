#Michael Kodel
#9/25/2026
#P2HW1
#String Formatting

#This is the title line for the program
print("This program calculates and displays travel expenses")
print()

#These are the user inputs for the program
budget = float(input("Enter your budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
accommodation = float(input("How much do you think you will spend on accommodation/hotel? "))
print()
food = float(input("How much do you think you will spend on food? "))
print()

#This is the title line for the output of the program
print("----------Travel Expenses----------")

#This is the formatted output of the program that displays the travel plan based on the user input
print(f"{'Location:':20} " + destination)
print(f"{'Initial Budget:':20} ${budget:.2f}")
print(f"{'Fuel:':20} ${gas:.2f}")
print(f"{'Accommodation:':20} ${accommodation:.2f}")
print(f"{'Food:':20} ${food:.2f}")
print("-----------------------------------")
print()
balance = budget - (gas + accommodation + food)
print(f"{'Remaining Balance:':20} ${balance:.2f}")
