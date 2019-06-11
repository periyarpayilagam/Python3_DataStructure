print(ord('a')) #unicode values , chr to unicode

x=chr(ord('a')+1) #unicode to char
print(x)

#char to bytes

m='d'
# char to bytes
n=bytes(m[0],'utf-8') # Unicode Transformation Format

print(n) #it says bytes d ans: b'd

#convert bytes into string

s=str(n)
print(s[0]) #b
print(s[1]) #'
print(s[2]) #d

data="abcd"

mynewdata=bytes(data,'utf-8')
print(mynewdata)  #b'abcd'












