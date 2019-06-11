class Calc:
    name="Casio"
    def __init__(self):
        self.name="anbu"
    def test(self,a,b):
        self.x=a
        self.y=b
        self.rate=200

class Test(Calc):
    def getValue(self):
        print(self.name)
        print(super.x)

obj1=Calc()
obj1.test(10,20)

obj2=Test()
obj2.getValue()



