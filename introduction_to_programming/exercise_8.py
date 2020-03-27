

### The program is about printing the total weight of your purchase od widgets and gizmos.






w = int(input("Enter the number of the widgets you have >> ")) # Ask the user for number of widgets ,here w is represented for widgets.
g = int(input("Enter the number of the gizmos you have >> ")) # Ask the user for number of gizmos ,here g is represented for gizmos .
x = ((w * 75) + (g * 112)) / 1000				     # Here i represent the total weight as x
print("The total weight of widgets and gizmos is %.3f kg " %x) # Prints the total weight with 3 decimal place in kilograms
