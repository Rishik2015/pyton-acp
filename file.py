# file=open("demo.txt","r")
# print(file.read())
# file.close()

fw=open("demo.txt","w")
fw.write("\n my name is rishik pathak.")
fw.write("\n i study in class 5.")
fw.close()

file=open("demo.txt","r")
print(file.read())

file.close()