#List Methods
list=["Tamil","English","Maths"]
print(list[0])
print(list[0:3])
print(list[-1:-3])

print(len(list))

list.pop()
print(list)

list.append("Maths")
print(list)

list.pop(1)
print(list)

list.insert(1,"English")
print(list)
del(list[0])
print(list)

list.extend(["Science","Social","Physics"])
print(list)

del(list[2])
print(list)

list.remove("Maths")
print(list)

list.reverse()
print(list)

print(list.count("Social"))
copy=list.copy()
print(copy)
clear=copy.clear()
print(clear)

list.sort()
print(list)

print(list.__contains__("Physics"))
list.__delitem__(0)

print(list)
item=list.__getitem__(0)

print(item)
L=[1,2,3]
del(L[0])
print(L)


L[2]="Science"





