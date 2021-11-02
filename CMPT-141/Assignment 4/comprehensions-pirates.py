prairie_pirates = [
    ['Tractor Jack', 1000, True],
    ['Plowshare Pete', 950, False],
    ['Prairie Lily', 245, True],
    ['Red River Rosie', 350, True],
    ['Mad Athabasca McArthur', 842, False],
    ['Assiniboine Sally', 620, True],
    ['Thresher Tom', 150, True],
    ['Cranky Canola Carl', 499, False]
]


# part a)
best_plunderers = [p[0] for p in prairie_pirates if p[1] > 400 ]

# part b)
parrot_haters = [p[0] for p in prairie_pirates if not p[2] ]

# part c)
plunder_values = [p[1] * 42 for p in prairie_pirates ]

# part d)
names_and_plunder_values = [[p[0], p[1] * 42] for p in prairie_pirates if p[2]]


print(best_plunderers)
print(parrot_haters)
print(plunder_values)
print(names_and_plunder_values)