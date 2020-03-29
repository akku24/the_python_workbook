

x = float(input("Enter the pressure in kilopascal >> "))
a = x * .15
b = x * 7.50062
c = x * .00986923 
print("Pressure in pounds per sq. inch is >> %.2f pounds/sq.inch"%a)
print("Pressure in millimeter of Hg is >> %.2f mm of Hg"%b)
print("Pressure in atmosphere is >> %.2f atm"%c)
