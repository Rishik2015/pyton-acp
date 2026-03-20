# li=[85,43,18,68,22,6,97,13,48,91]
# for i in li:
#     if i%2==0:
#         print(i)

# Program to check triangle type

# Input sides
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Check if it's a valid triangle first
if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print("The triangle is Equilateral.")
    
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    
    else:
        print("The triangle is Scalene.")

else:
    print("The given sides do not form a valid triangle.")

        


            