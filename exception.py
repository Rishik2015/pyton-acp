def check_age():
    while True:
        try:
            val = input("Enter your age: ")
            age = int(val) # Triggers ValueError if not a number
            
            if age < 0 or age > 120:
                raise ValueError("Age must be between 0 and 120.")
            
            # Check for even or odd
            if age % 2 == 0:
                print(f"{age} is an Even number.")
            else:
                print(f"{age} is an Odd number.")
            
            break # Exit loop if successful
            
        except ValueError as e:
            print(f"Invalid input: {e}")

check_age()