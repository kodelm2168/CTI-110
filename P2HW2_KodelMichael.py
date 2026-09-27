#Michael Kodel
#09/26/2026
#P2HW2
#This program will have the user enter test grades for 6 modules and then display the lowest grade, highest grade, and the average grade.


#Empty List
grades = []

#Ask for the grades for each module and add to list
module_1 = float(input("Enter the grade for module 1: "))
grades.append(module_1)
module_2 = float(input("Enter the grade for module 2: "))
grades.append(module_2)
module_3 = float(input("Enter the grade for module 3: "))
grades.append(module_3)
module_4 = float(input("Enter the grade for module 4: "))
grades.append(module_4)
module_5 = float(input("Enter the grade for module 5: "))
grades.append(module_5)
module_6 = float(input("Enter the grade for module 6: "))
grades.append(module_6)

#Display the lowest grade, highest grade, sum of grades, and average grade 
min_grade = min(grades)
max_grade = max(grades)
sum_grades = sum(grades)
average_grade = sum_grades / len(grades)

print("-------------Results------------")
print(f"{'Lowest grade:':25} {min_grade:.1f}")
print(f"{'Highest grade:':25} {max_grade:.1f}")
print(f"{'Sum of grades:':25} {sum_grades:.1f}")
print(f"{'Average grade:':25} {average_grade:.2f}")
print("--------------------------------")