class Dog:
     
     species = 'dog'

     def __init__(self,name,age):
          self.name = name
          self.age = age
     def bark(self):
          print(self.name," can bark")   

# an object 
rocky = Dog("rocky", 10)      
fooky = Dog("focky", 15)    
# class attrribute 
print("rocky is a {}" .format(rocky.species))   
print("fooky is a {}" .format(fooky.species))   
# instance attributes  
print("{} is {} years old".format(rocky.name,rocky.age))
print("{} is {} years old".format(fooky.name,fooky.age))

rocky.bark()