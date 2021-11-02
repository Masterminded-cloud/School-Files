
def trip_cost(airfare,room_cost,number_of_people,number_of_nights):

"""
    Calculates the total cost of the trip for the group
 based on double occupancy
       airfare: (float) cost of flight per person in dollars
       room cost: (float) cost for a double room in dollars
       number_of_people: (int) for the trip
       number_of_nights: (int) on the trip
"""
       total_hotel_cost  = (number_of_people // 2 + number_of_people % 2) * room_cost * number_of_nights
       return number_of_people * airfare + total_hotel_cost

print("Calculate Trip Cost")
air = float(input("Enter cost of flight ($): "))
hotel_per_night = float(input("Enter cost of a double room per night: "))
people = int(input("Enter the number of people: "))
nights = int(input("Enter the number of nights: "))

print("The total cost of the trip for the group is $", trip_cost(air,hotel_per_night,people,nights))
