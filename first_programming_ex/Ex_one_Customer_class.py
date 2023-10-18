"""
The objective of this task is to create a class to handle a customer loyalty program.

The program tracks the purchases for customers and recognizez that if a customer accumulates more than 100USD in purchases, 
the customer gets a 10USD discount on the next purchase. Then resets the 10USD discount deal.

The methods are:
    - makePurchase(), param = (self, amount), which registers a purchase for the customer.
    - discountReached(), param = (self), which checks whether the customer have earned a discount or not.
"""

class Customer: ## defining the clss
    def __init__(self): ## defining the constructor within the class
        self._total_purchases = 0 ## Instance variable. Is protected because the total purchase should not be manipulated by users.
        self._has_discount = False ## Instance variable. Is protected because whether the customer has a discount or not should not be manipulated by user.

## Methods used in this class
    def makePurchase(self, amount): ## This method only takes one purchase as parameter at the time, the parameter is of the type float.
        
        if self._has_discount:
            amount = max(0, amount - 10) ## If the customer has a discount, deduct 10USD from the purchase. Using max to avoid negative amount.
            self._has_discount = False ## Resets the discount to False if used.

        self._total_purchases += amount ## Add purchase to total purchase amount for the customer.

        if self._total_purchases >= 100: ## The if statement evaluates the logical operator to see if the total_purchase amount is above 100USD.
            self._total_purchases = 0 ## If the statement is true, reset the balance to zero.
            self._has_discount = True ## If the statement is true, give the customer a 10USD discount which is stored to the next purchase. 

    def discountReached(self): ## This method checks whether the customer has a discount to use on the next purchase.
        return self._has_discount

        
## Test Program 
customer = Customer() ## Create an instance variable from the Customer class.
    
## Test a scenario
purchases = [60, 40, 95, 20] ## Define the purchases as a list. 60, no disc, 60+40, disc, 95-10 = 85, no disc, 85+20=105, disc
for purchase in purchases: ## Loop trough the list using the program written above
    customer.makePurchase(purchase) ## Make purchases based on the list of purchases
    print(f"After a purchase of ${purchase}, has discount: {customer.discountReached()}") ## Print the purchase value and if the customer has a discount.