class square:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self) :
        print("Area of square=",self.length+self.width*2) 

ri1=square(10,2)
ri1.area()