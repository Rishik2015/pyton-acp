class Parrot:
     
     species = 'bird'

     def __init__(self,name,age):
          self.name = name
          self.age = age
     def speak(self):
          print(self.name," can speak")   

# an object 
goo = Parrot("goo", 10)      
fuu = Parrot("fuu", 15)    
# class attrribute 
print("goo is a {}" .format(goo.species))   
print("fuu is a {}" .format(fuu.species))   
# instance attributes  
print("{} is {} years old".format(goo.name,goo.age))
print("{} is {} years old".format(fuu.name,fuu.age))

goo.speak()

