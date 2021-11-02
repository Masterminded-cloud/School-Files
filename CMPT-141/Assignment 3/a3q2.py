
import math as m


debt = float(input('Enter amount of debt in dollars: '))

while debt <= 0:

    print('Error!  Debt must be a positive number.')

    debt = float(input('Enter amount of debt in dollars: '))



month = 1

current_payment = debt


while current_payment <= 100*debt:

    current_payment = debt + debt * (m.pow(2, month) / 100)

    print('After', month, 'months, you owe: ' "$"+str(current_payment))

    month = month + 1


print("Time to pay up!")

