

### The program is about conversion of heigths in feets to centimeters but here as per S.I unit ill convert it into meters.

x,y = map(int,input("Enter your height in feets with inchs >> ").split()) 
h = (x * 12 * 2.54) + (y * 2.54)
print("The given height in meters is >> %.3f m "%h)
