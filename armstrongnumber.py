num=int(input("Please enter a number:"))
sum=0
a=num
numofnum=len(str(num))
while a>0:
    digit=a%10
    sum+=digit**numofnum
    a//=10
if num==sum:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
