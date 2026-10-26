#Michael Kodel
#10/26/2026
#P4LAB2
#Use for and while statements to create a multiplication table


run_again = 'yes'

while run_again != "no":
    #Get user input
    user_num = int(input("Enter an integer: "))
    
    if user_num >= 0:
        #Print multiplication table for the user number
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("Please enter a positive integer.")
    
    # Ask user if they want to run the program again
    run_again = input("Do you want to run the program again? ")

#User entered 'no'
print("Program is ending.....")