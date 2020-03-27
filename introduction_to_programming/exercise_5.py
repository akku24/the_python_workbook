
### The program is about calculating the refund for depostion of used bottle.





a = int(input("Enter the number of bottles upto one litre >> ")) # We can taking input of bottles less than or equal to one litre.
b = int(input("Enter the number of bottles above one litre >> ")) # We can taking input of bottles more than one litre.
r = (a * 0.10) + (b * 0.25) # Here r is refund amount.
print("The refund amount is $%.2f"%r) # Printing out the refund amount to the user.
