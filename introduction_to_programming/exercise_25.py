

t = int(input("Enter the total number of seconds >> "))
d = t // (24 * 3600)
h = (t % (24 * 3600)) // 3600
m = ((t % (24 * 3600)) % 3600) // 60
s = (((t % (24 * 3600)) % 3600 ) % 60) 
print("DD:HH:MM:SS >>%d:%d:%d:%d"%(d,h,m,s))
 
