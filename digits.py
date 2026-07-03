num = int(input("Enter a number: "))
if num < 0:
    num = -num
if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
print("The number of digits =", count)
#or you can do this
num=int(input("Please enter a number:"))
print("The number of digits =", len(str(num)))