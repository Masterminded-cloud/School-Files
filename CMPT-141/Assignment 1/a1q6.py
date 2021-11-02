
# Obtain the total fee and the number of staff
total_fee = float(input('Enter the payment for the case:  '))
number_of_staff = int(input('Enter the number of staff:  '))

# Display the results of the computations
print("Phoenix Wright's 25% share of the fee is worth:", '$'+str(total_fee*0.25))
print("The staff's 75% share of the fee is worth:", '$'+str(total_fee*0.75))
print("Each staff member takes home:", '$'+str((total_fee*0.75)/number_of_staff))



