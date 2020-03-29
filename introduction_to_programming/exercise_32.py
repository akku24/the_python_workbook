a = int(input("Enter a four digit number >>"))
b = a / 1000 
c = (a % 1000) / 100
d = ((a % 1000) % 100) / 10
e = (((a % 1000) % 100) % 10)
s = b + c + d + e
print("%d + %d + %d + %d = %d "%(b,c,d,e,s)) 
