class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def display(self):
        print(self.stack)

    def remove(self):
        self.stack.pop()

    def size(self):
        print(len(self.stack))

obj = Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.display()
obj.remove()
obj.display()
obj.size()


