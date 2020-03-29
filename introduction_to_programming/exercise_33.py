

a,b,c = map(int,input("Enter three integer to sort >> ").split())
x = max(a,b,c)
y = min(a,b,c)
z = a + b + c - x -y
print("After sorting >> %d -> %d -> %d"%(y,z,x))
