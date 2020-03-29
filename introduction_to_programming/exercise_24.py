
d,h,m,s = map(float,input("Enter number of days,hours,minutes,second >> ").split())
t = d * 24 * 3600 + h * 3600 + m * 60 + s
print("Total number of seconds are  >> ",t)
