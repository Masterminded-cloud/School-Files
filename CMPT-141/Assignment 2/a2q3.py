

def calculate_speed(distance, time):

    """

    returns speed of object


    distance: (int) distance traveled

    time: (int) time taken

    """

    speed = distance // time

    return speed



print("Calculate Speed")


distance = int(input("Enter desired distance (km): "))

time = int(input("Enter desired time (hours): "))

speed = calculate_speed(distance, time)

print("In order to travel " + str(distance) + " km in " + str(time) + " hours you must travel at " + str(speed) + " km/h.")
