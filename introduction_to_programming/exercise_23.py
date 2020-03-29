

from math import tan,pi
s,n = map(float,input("Enter the length and number of sides >> ").split())
area = (n * s ** 2) / (4 * tan(pi / n))
print("Area of gievn polygon is >> %.3f sq m"%area)
