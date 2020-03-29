p,v,t=map(float,input("Enter pressure,volume and temperature  >> ").split())
n = (p * v)/(8.314 * t)
print("The number of moles in given volume of gas is >> %.3f"%n)
