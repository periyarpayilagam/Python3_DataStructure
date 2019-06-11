d=dict([('name','guhan'),('age',28)])
print(d)
d={'name':'guhan','age':27}
print(d)

d={'name':'guhan'}
print(d)
d.update({'name':'anbu'}) #update same key not includes new key
print(d)

print(d['name'])
d['name']='raja'
print(d)
d.update({'mob':7687}) # new dict
print(d)
print(d.get('name'))
d.pop('age')
print(d)
d.popitem() #removes from last key and values
print(d)
d.popitem()
print(d)
d.update({'name':'anbu'})
print(d)

