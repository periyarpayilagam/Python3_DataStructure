num=int(input("Enter any number"))
sum=0
count=0
while num>0:
    rem =num%10
    sum=sum+rem*(8**count)
    print(rem)
    num=num//10
    count=count+1

print("The Decimal number is: ", sum)
