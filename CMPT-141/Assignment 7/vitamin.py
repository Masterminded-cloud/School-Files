import random as rand

def smash(W):
	'''
	Returns the number of pieces that a pokemon team can get from a vitamin weighing W grams.
	W: the weight of the vitamin
	return: the number of pieces
	'''
	if W <= 0.1:
		return 1
	else:
		pieces = rand.randint(2,4)
		total = 0
		for p in range(pieces):
			total = total + smash(W/pieces)
		return total

W = float(input("How big is the vitamin, in grams? "))

total = 0
for i in range(1000):
	total = total + smash(W)
print('On average, a pokemon team can get', total/1000, 'bite-sized pieces from a', W, 'gram vitamin!', )
