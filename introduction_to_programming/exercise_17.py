m = float(input("Enter the mass of water in grams >> "))
t = float(input("Enter the temperature difference in degree celcius >> "))
q = m * 4.186 * t
print("The total amount of energy required  is >> %.3f J"%q)
amt = q * 0.0000002778 * 8.9 
print("Cost of electricity used is = %.4f cents"%amt)
