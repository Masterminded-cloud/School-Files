
import matplotlib.pyplot as plt

def supply( price ):

    """

    Returns the quantity of special edition units supplied when selling it at given price.

    price: The price each special edition is sold for.

    return: The quantity of special edition units supplied by the publisher.

    """

    return 500 + 90*price



def demand( price ):

    """

    Returns the demanded quantity of special edition units for a given selling price.

    price: The price each special edition is sold for.

    return: The quantity demanded of special edition units.

    """
    return 10000 - 35*price





plt.figure()


for P in range(10,160):
	
	print(P, supply(P), demand(P))
   

	plt.plot(P, supply(P), 'og')

	plt.plot(P, demand(P), 'ob')


	if supply(P) == demand(P):

		optimal_price = P

		plt.plot(P, supply(P), 'or')
print('The optimal selling price of $' + str(optimal_price), 'will result in the sale of', supply(optimal_price), 'units.')




plt.xlim(0, 170)

plt.ylim(0, 16000)


plt.xlabel("Price of Special Edition (dollars)")

plt.ylabel("Quantity Produced (units)")

plt.title("Price of Special Edition VS Quantity Produced")




plt.annotate("Optimal Price",(optimal_price,supply(optimal_price)))
figures
plt.show()

