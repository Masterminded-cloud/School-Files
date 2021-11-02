

def revenue( donations,n_lemonades,price_per_lemonade ):

    """

       The amount of income earned from the lemonade stand.


       donations: Amount of money received as donations

       n_lemonades: Number of lemonades sold.
   
    price_per_lemonade: The selling price for one lemonade.
   

    return: The total income earned.

    """

	return donations + n_lemonades*price_per_lemonade



def costs( n_lemons,cost_per_lemon ):
    
    """

       The amount of expenses incurred from running the lemonade stand.


       n_lemons: Number of lemons used to make lemonade.
   
    cost_per_lemon: Price per lemon bought.


       return: The total expenses incurred.
  
    """
    
	return n_lemons*cost_per_lemon



def profit( donations,n_lemonades,price_per_lemonade,n_lemons,cost_per_lemon ):
    
    """
   
    The net amount of money earned from the lemonade stand.

       donations: Amount of money received as donations

       n_lemonades: Number of lemonades sold.

       price_per_lemonade: The selling price for one lemonade.
   
    n_lemons: Number of lemons used to make lemonade.
   
    cost_per_lemon: Price per lemon bought.


       return: The net income earned.

    """

	total_revenue = revenue(donations,n_lemonades,price_per_lemonade)

	total_costs = costs(n_lemons,cost_per_lemon)

	return total_revenue - total_costs



# ask user for relevant inputs


n_lemons = int(input("How many lemons were used?: "))

cost_per_lemon = float(input("What was the cost per lemon (in dollars)?: "))

n_lemonades = int(input("How many lemonades were sold?: "))

price_per_lemonade = float(input("What was the selling price of one lemonade (in dollars)?: "))

donations = float(input("How much money did you receive in donations (in dollars)?: "))



# print results of running the lemonade stand for given inputs


print("Revenue: $"+str(revenue(donations,n_lemonades,price_per_lemonade)))

print("Costs: $"+str(costs(n_lemons,cost_per_lemon)))

print("Profit: $"+str(profit(donations,n_lemonades,price_per_lemonade,n_lemons,cost_per_lemon)))
