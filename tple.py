def multiply_tuple(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

my_tuple = (2, 3, 4, 5)
print(f"The product is: {multiply_tuple(my_tuple)}")