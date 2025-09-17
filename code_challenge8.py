#MULTIPLICATION TABLE MAKER

print("MULTIPLICATION TABLE MAKER")

number = eval(input("Enter a number -->"))

print("\nMultiplication table for", number)

for k in range(1, 11):  
	print(number, "x", k, "=", number * k)
