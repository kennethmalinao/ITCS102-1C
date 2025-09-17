#Starting Countdown

number = eval(input("Enter a number where you want the countdown to start --> "))

print("\nHere is the countdown --> ")

for k in range(number, 0,-1):
    print(k)
print("Liftoff!")