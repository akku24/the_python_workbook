


### The program is to tell user their total cost of meal with and without the tax and tip.




cost = int(input("Enter the cost of meal without the tax and tip >>")) # Here we take input from user.
amt = cost + (cost * .05) + (cost * .18) 			    # It calculate the tax and tip and adds with the original price.
print("The total cost the meal with tax and tip is %.2f"%amt) 	    # It prints out the toatl cost.



