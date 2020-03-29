from math import sqrt
a,b,c = map(float,input("Enter the sides of triangle >> ").split())
s = (a + b + c)/2
area = sqrt(s * (s-a) * (s-b) * (s-c))
print("The area of given triangle is >> %.3f sq m"%area)
