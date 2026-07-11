import tkinter as tk

def get_name():
    typed_name = name_entry.get()
    print("Hello,", typed_name + "!")

root = tk.Tk()
root.title("enter a measurement in inchees")

name_entry = tk.Entry(root)
name_entry.pack()

my_button = tk.Button(root, text="Say Hello", command=get_name)
my_button.pack()

typed_name = typed_name // 2.54

root.mainloop()