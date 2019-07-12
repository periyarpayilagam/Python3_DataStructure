d={
    'name':'raja',
    'age':26,
    'mob':6576
}
print(d.get('name'))

d['name']="Anbu"
print(d)

d.pop('age')
print(d)

for i in d:
    print(i)

for i in d.keys():
    print(i)

for i in d.values():
    print(i)

for i,j in d.items():
    print(i,j)







