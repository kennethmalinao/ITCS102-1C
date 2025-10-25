k = 6
for i in range(1, k+1):
    print("  " * (k - i), end="")

    for x in range(i, 1, -1):
        print(x, end=" ")
    print("1", end=" ")

    for y in range(2, i+1):
        print(y, end=" ")
    print()