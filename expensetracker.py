expenses = []

print("Mini Expense Predictor")
print("Type 'done' when finished.\n")

while True:
    entry = input("Enter expense: ")

    if entry.lower() == "done":
        break

    try:
        expenses.append(float(entry))
    except ValueError:
        print("Please enter a valid number.")

if len(expenses) == 0:
    print("No expenses entered.")
else:
    total = sum(expenses)
    days = len(expenses)
    average = total / days
    monthly_prediction = average * 30

    print("\n----- Report -----")
    print(f"Days Recorded: {days}")
    print(f"Total Spent: ₹{total:.2f}")
    print(f"Average Per Day: ₹{average:.2f}")
    print(f"Predicted Monthly Expense: ₹{monthly_prediction:.2f}")