def spaceTime(dist):
    '''
    Calculate the time required by the Team Rocket drive to travel a given distance
    :param dist: the distance to travel in meters
    :return: The number of minutes to travel dist meters
    '''
    if dist <= 1:
        return 1
    else:
        return 1 + spaceTime(dist/2)

examples = [{'destination' : "to the nearest Poke-Stop", 'distance' : 37},
            {'destination' : "for a round-trip around the earth", 'distance' : 40075000.0},
            {'destination' : "from our earth to our sun", 'distance' : 1.49e11},
            {'destination' : "from our sun to the nearest star", 'distance' : 4.0e16},
            {'destination' : "across the observable universe", 'distance' : 8.8e26}
            ]

print("Team Rocket's drive requires:")

for e in examples:
    print("-", spaceTime(e['distance']),
          "minutes to travel", e['distance'], 'meters',
          e['destination'])

print("\nWOW, IS TEAM ROCKET EVER BLASTING OFF AGAIN!!")

