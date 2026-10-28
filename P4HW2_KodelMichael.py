#Michael Kodel
#10/27/2026
#P4HW2
#

#Prompt user for employee's name, hours worked, and hourly pay rate
employee_name = input("Enter employee's name or 'done' to finish: ")

#Create accumulator variables for overtime pay, regualr pay, gross pay and employee count
ot_pay_total = 0
reg_pay_total = 0
gross_pay_total = 0
employee_count = 0

while employee_name != 'done':
    #Add employee count
    employee_count += 1
    #Ask for employee info
    hours_worked = float(input("How many hours did " +employee_name+ " work this week? "))
    hourly_pay_rate = float(input("What is " +employee_name+ "'s hourly pay rate? "))

 
    #Evaluate overtime
    if hours_worked <=40:
        regular_pay = hours_worked * hourly_pay_rate
        overtime_pay = 0
    else:
        regular_pay = 40 * hourly_pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (hourly_pay_rate * 1.5)

    #Add to accumulators
    ot_pay_total += overtime_pay
    reg_pay_total += regular_pay
    gross_pay_total += regular_pay + overtime_pay

    #Display the results in a formatted table
    print("----------------------------------")
    print("Employee Name: ", employee_name)
    print()
    print(f'{"Hours Worked":<15}{"Pay Rate":<11}{"Overtime Hours":<18}{"Overtime Pay":<15}{"Regular Pay":<15}{"Total Pay":<15}')
    print("----------------------------------------------------------------------------------")
    print(f'{hours_worked:<15.2f}{hourly_pay_rate:<11.2f}{overtime_hours if hours_worked > 40 else 0:<18.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{regular_pay + overtime_pay:<15.2f}')


    employee_name = input("Enter employee's name or 'done' to finish: ")

print("total number of employees processed: ", employee_count)
print("Total amount paid for overtime: $", format(ot_pay_total, ",.2f"))
print("Total amount paid for regular pay: $", format(reg_pay_total, ",.2f"))
print("Total amount paid for gross pay: $", format(gross_pay_total, ",.2f"))