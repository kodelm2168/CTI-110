# Michael Kodel
# 9/4/2026
# P1HW1
# This program will calculate exponents, addition, and subtraction based on user input.

print("-----Calculating Exponents-----") 
print()

base = int(input("Enter a base number:"))
exponent = int(input("Enter an exponent number:"))
result = base ** exponent
print()
print(base, "raised to the power of", exponent, "is", result, "!!")
print()

print("-----Addition and Subtraction-----")
print()

starting_number = int(input("Enter a starting number:"))
add_number = int(input("Enter a number to add:"))
subtract_number = int(input("Enter a number to subtract:"))
addsubtract_result = starting_number + add_number - subtract_number
print()
print(starting_number, "+", add_number, "-", subtract_number, "is equal to", addsubtract_result, "!!")
print()