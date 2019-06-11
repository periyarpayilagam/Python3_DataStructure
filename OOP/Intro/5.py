class Calc: 
    name="Casio"
    def add(self): #can't call without using 'self'
        print("Hi")
    def test(self,a,b):
        self.x=a
        self.y=b
        print(self.x,self.y)
    def getValue(self):
        print(self.x)
        print(self.y)
        
obj=Calc()
obj.name
obj.add()
obj.test(10,20)
obj.getValue()




