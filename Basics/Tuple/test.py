t=tuple([2,4,6,7,5,8])
print(t)
print(len(t))
print(t[0])
print(t[0:3])
#del(t) #for deleting object
#print(t)
a = any(t)
print(a)
#print(sorted(t))
s=sorted(t)
print(s)
print(min(t))
print(max(t))
print(sum(t))
print(enumerate(t))
print(t.count(4))
print(t.index(4))
print(t.__add__((4,9)))
print(t.__contains__(2))
for i,j in enumerate(t):
    print(i,j)
