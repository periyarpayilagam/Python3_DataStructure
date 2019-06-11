#sum of numbers
num=235236
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
print(sum)
