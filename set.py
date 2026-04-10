set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Method 1: Using the ^ operator
result = set_a ^ set_b

# Method 2: Using the symmetric_difference() method
# result = set_a.symmetric_difference(set_b)

print(f"The symmetric difference is: {result}")