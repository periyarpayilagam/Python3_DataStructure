class College:
    
    def __init__(self,x,y,z):
        self.name=x
        self.age=y
        self.mark=z 
        
    def getDetails(self):
        print(self.name)
        print(self.age)
        print(self.mark)
        
raja =College("Raja",23, 67)
#raja.getDetails()

anbu=College("Anbu",22,65)
#anbu.getDetails()

surya=College("Surya",26,74)
#surya.getDetails()

temp=College("x",4,5)
#temp.getDetails()

temp=raja
#raja.getDetails()

arr=[raja,anbu,surya]

for i in range(0,len(arr)):
    for j in range(0, len(arr)):
        if arr[i].mark>arr[j].mark:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

for i in range(0,len(arr)):
    print("rank",(i+1))
    print("Name ",arr[i].name)
    print("Age ",arr[i].age)
    print("mark ", arr[i].mark)

"""

rank 1
Name  Surya
Age  26
mark  74
rank 2
Name  Raja
Age  23
mark  67
rank 3
Name  Anbu
Age  22
mark  65

"""

