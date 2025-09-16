#Get the factorial of a number

number = eval(input("Enter a number -->"))
factorial = 1
for k in range (number,0,-1):
	print(k)
	factorial *= k
print("The factorial of a number is", factorial)

