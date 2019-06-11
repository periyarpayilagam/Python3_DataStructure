name="guhan"
if name=="guhan":
    print("His name is Guhan")

print("Enter Salary")
salary =input()
salary=int(salary)
if salary==0 or salary<0:
    print("sholud be greater than zero")

elif salary>0 and salary<1000:
    print("Give 10% bonus")

else:
    print("give 30% bonus")

