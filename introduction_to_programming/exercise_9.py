







p = float(input("Enter the principal amount >> ")) # Input of our intial amount.
t = int(input("Enter the number of years of your savings account >> ")) # Input of number of years of your savings account.
for t in range(1,t+1):           # Its for printing the amiunt
	a = p * (1 + 0.04) ** t
	print(f"Your balance after addition of 4 percent is intrest after {t} years is >> {} rupees",t,a) # Prints each years balance amount
print("The final balance is %.2f "%a ) # Prints the final balance in your account
