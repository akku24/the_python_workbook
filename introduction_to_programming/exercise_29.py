
from math import floor
t = float(input("Enter the air temperature in degree celsius >> "))
s = float(input("Enter the air speed in km/h >> "))
if t <= 10 or s > 4.8 :
	wcl = 13.12 + (0.6215 * t) - (11.37 * (s ** .16)) + (.3965 * t * (s ** .16))
	print("The wind chill index for given temperature and spped is >> ",floor(wcl)) 
else :
	print("Data is invalid....")

