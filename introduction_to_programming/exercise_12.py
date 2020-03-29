

### This program is to find the distance between the two coordinate .


from math import sin,cos,acos,radians
a,b=map(float,input("Enter the coordinates of first place in degrees >> ").split())
a1,b1=map(float,input("Enter the coordinates of second place in degrees >> ").split())
t1 = radians(a)
t2 = radians(a1)
g1 = radians(b)
g2 = radians(b1)
dist = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))
print("Distance between two cordinates in km is >>  ",round(dist,3))
