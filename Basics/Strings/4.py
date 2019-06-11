x="Chennai is a city"
#print("lengths is:", len(x))
#print(x.lower())
#print(x.upper())
#print(x.capitalize())
#print(x.swapcase())
#print(x.replace("is","es"))
#print(x.center(10,"*"))
#print(x.find("n"))
#print(x.find('z'))
#print(x.index('n'))
#print("*".join(x))
#print(x.rstrip("-"))
#print(x.split())
#print(list(x))


x="QWERTY"

print(len(x))

print(x.lower())

print(x.upper())

print(x.capitalize())

print(x.swapcase()) #if lower means upper, upper means lower

print(x.center(8,'_'))

print(x.count('Q'))

print(x.find('W')) # found 1

print(x.find('Z')) # not found -1

print(x.index('E'))

s=("A","B","C","D")
print("-".join(s))

data="---ABCD   --- ABCD  ---"
print(data.strip())
print(data.lstrip("-"))
print(data.rstrip("-"))
print(data.strip("-")) #strip both left and right

print(x.split()) #list of substring

print(x.replace("Q","P"))

"""    6
    qwerty
    QWERTY
    Qwerty
    qwerty
    _QWERTY_
    1
    1
    -1
    2
    A-B-C-D
    ---ABCD   --- ABCD  ---
    ABCD   --- ABCD  ---
    ---ABCD   --- ABCD
    ABCD   --- ABCD
    ['QWERTY']
    PWERTY
"""