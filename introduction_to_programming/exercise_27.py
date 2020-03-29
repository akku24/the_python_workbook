

from math import floor
year = int(input("Enter year >> "))
a = year % 19
b = floor(year / 100)
c = year % 100
d = floor(b / 4)
e = b % 4
f = floor((b + 8) / 25)
g = floor((b - f + 1 ) / 3)
h = (19 * a + b - d - g + 15) % 30
i = floor(c / 4)
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = floor((a + 11 * h + 22 * l) / 451)
month = floor((h + l - 7 * m + 114) / 31)
day = 1 + ((h + l - 7 * m + 114) % 31)
if month == 1 :
	month = 'January'
elif month == 2 :
	month = 'February'
elif month == 3 :
	month = 'March'
elif month == 4 :
	month = 'April'
elif month == 5 :
	month = 'May'
elif month == 6 :
	month = 'June'
elif month == 7 :
	month = 'July'
elif month == 8 :
	month = 'August'
elif month == 9 :
	month = 'September'
elif month == 10 :
	month = 'October'
elif month == 11 :
	month = 'November'
else :
	month = 'December' 
print("Easter will come on %d th of %s in %d year"%(day,month,year))
