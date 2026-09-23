#Michael Kodel
#9/23/2026
#P2LAB1
#This program will take the users input for the radius of a circle and calculate the diameter, circumfrence and area

#Import the math module to use math.pi
import math

#Get the radius from the user
radius = float(input("Enter the radius of the circle: "))
print()

#calulate the diameter of the circle and display to 1 decimal point
diameter = 2 * radius
print(f"The diameter of the circle is {diameter:.1f}\n")

#Calculate the circumference of the circle and display to 2 decimal points
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is {circumference:.2f}\n")

#Calculate the area of the circle and display to 3 decimal points
area = math.pi * radius ** 2
print(f"The area of the circle is {area:.3f}\n")
