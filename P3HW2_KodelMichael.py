#Michael Kodel
#10/9/2026
#P3HW2
#Salary Calculator



#Prompt user for employee's name, hours worked, and hourly pay rate
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))


#Calculate regular pay and overtime pay
if hours_worked <=40:
    regular_pay = hours_worked * hourly_pay_rate
    overtime_pay = 0
else:
    regular_pay = 40 * hourly_pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (hourly_pay_rate * 1.5)

#Display the results in a formatted table
print("----------------------------------")
print("Employee Name: ", employee_name)
print()
print(f'{"Hours Worked":<15}{"Pay Rate":<11}{"Overtime Hours":<18}{"Overtime Pay":<15}{"Regular Pay":<15}{"Total Pay":<15}')
print("----------------------------------------------------------------------------------")
print(f'{hours_worked:<15.2f}{hourly_pay_rate:<11.2f}{overtime_hours if hours_worked > 40 else 0:<18.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{regular_pay + overtime_pay:<15.2f}')