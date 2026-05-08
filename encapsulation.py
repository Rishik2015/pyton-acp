s = input("enter a string ")
r = ""

class String :
    def __init__(self , string):
        self.string = string

        for i in s:
            r=r+i
    print("Originaaal string ",s) 
    print("Reversed string",r)       