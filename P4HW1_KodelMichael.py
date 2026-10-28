#Michael Kodel
#10/27/2026
#P4HW1
#Using a for loop, this program will have the user enter test grades for a number of modules and then display the lowest grade, 
# list of grades, average grade, and letter grade.


#Empty List
grades = []

#Ask for the number of grades the user wants to enter
num_grades = int(input("How many grades would you like to enter? "))

#For loop to get the grades from the user and add them to the list, while removing invalid grades
for i in range(num_grades):
    grade = float(input(f"Enter the grade for module {i + 1}: "))
    if grade < 0 or grade > 100:
        print("Invalid grade entered. Please enter a grade between 0 and 100.")
         
        grade = float (input(f"Enter the grade for module {i + 1} again: "))
        grades.append(grade)
    else:
        grades.append(grade)


min_grade = min(grades)
grades.remove(min_grade)
avg_grade = sum(grades) / len(grades)

if avg_grade >= 90:
    letter_grade = "A"
elif avg_grade >= 80:
    letter_grade = "B"
elif avg_grade >= 70:
    letter_grade = "C"
else:
    letter_grade = "F"


#Print the lowest grade, list of grades, score average, and letter grade
print("-------------Results------------")
print(f"{'Lowest grade:':15} {min_grade:.1f}")
print(f"{'List of grades:':15} {grades}")
print(f"{'Average grade:':15} {avg_grade:.2f}")
print(f"{'Letter grade:':15} {letter_grade}")
print("--------------------------------")