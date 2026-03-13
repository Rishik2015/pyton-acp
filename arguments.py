
#Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.

# def total_calc(bill_amount,tip_perc):

#     total = bill_amount*(1 + 0.01*tip_perc)
#     total = round(total,2)
#     print(f"please pay ${total}")
    
# total_calc(167,67)    

# def cube(number):
#     return number*number*number
# def by_three(number):
#     if number %3==0:
#         return cube(number)
#     else:
#         return False
    

# print(by_three(9))
# print(by_three(4))



def factorial(x):
    """this is a recursive function to find the factorial of an integer"""
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("The factorial of 0:",factorial(0))
print("The factorial of 10:",factorial(10))