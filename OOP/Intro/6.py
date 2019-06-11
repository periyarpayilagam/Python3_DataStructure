class Calc:
    r=23
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def getValue(self):
        print(self.x)
        print(self.y)
    def test(self,m,n):
        self.m1=m
        self.n1=n
    def test1(self):
        print(self.m1)
        print(self.r)
        self.r=67
    def test2(self):
        print(self.r)

obj=Calc(10,20)
obj.getValue()
obj.test(100,200)
obj.test1()
obj.test2()
