import math as m

# Part (a): Read in the height from the console
H = float(input('From what height is the computer dropped?  '))

# Part (b): Calculate the time of impact
time_to_impact = m.sqrt(2*H/9.8)

# Part (c): Display the results of the computation.
print('There is a satisfying explosion of circuitry!')
print('The computer dropped from', H, 'meters hits the ground after', time_to_impact, 'seconds.')

