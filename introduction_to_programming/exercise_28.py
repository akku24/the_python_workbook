

a = int(input("If have height in inches and weight in pounds enter 1 \n Or in height in meters and weight in kilograms enter 2 \n >>>>"))
if a == 1 :
	w = float(input("Enter the weight in pounds >> "))
	h = float(input("Enter the height in inches >> "))
	bmi = (w * 703) / (h ** 2)
	print("The BMI is >> %.1f"%bmi)
elif a == 2 :
	w = float(input("Enter the weight in kilogram>> "))
	h = float(input("Enter the height in meters >> "))
	bmi = w / (h ** 2)
	print("The BMI is >> %.1f"%bmi)
else :
	print("Invalid Input")
