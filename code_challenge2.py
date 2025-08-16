amount = eval(input("Enter the amount .... "))
print("Here is a breakdown of your deposit")

thousand = amount // 1000
amount = amount % 1000
print(thousand, "\t-\t1000")

fhundred = amount // 500
amount = amount % 500
print(fhundred, "\t-\t500")

thundred = amount // 200
amount = amount % 200
print(thundred, "\t-\t200")

hundred = amount // 100
amount = amount % 100
print(hundred, "\t-\t100")

fifty = amount // 50
amount = amount % 50
print(fifty, "\t-\t50")

twenty = amount // 20
amount = amount % 20
print(twenty, "\t-\t20")

ten = amount // 10
amount = amount % 10
print(ten, "\t-\t10")

five = amount // 5
amount = amount % 5
print(five, "\t-\t5")

one = amount // 1
amount = amount % 1
print(one, "\t-\t1")



