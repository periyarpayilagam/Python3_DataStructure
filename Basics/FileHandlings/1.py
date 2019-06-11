#create new text file
#open("myfile1.txt","w")
f=open("myfile.txt","w")
f.write("Welcome")

#print multiple lines

for i in range(1,11):
   f.write("The text line is {} \n".format(i))

