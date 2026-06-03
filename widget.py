import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        label_result.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x200")

label1 = tk.Label(root, text="Enter First Number:")
label1.pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter Second Number:")
label2.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

button_multiply = tk.Button(root, text="Multiply", command=calculate_product)
button_multiply.pack(pady=10)

label_result = tk.Label(root, text="Product: ")
label_result.pack(pady=5)

root.mainloop()
