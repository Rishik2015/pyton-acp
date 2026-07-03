import tkinter as tk

def calculate():
    p = float(entry_p.get())
    r = float(entry_r.get())
    t = float(entry_t.get())
    si = (p * r * t) / 100
    lbl_result.config(text=f"Interest: {si} | Total: {p + si}")

root = tk.Tk()
root.title("SI Calc")

tk.Label(root, text="Principal:").pack()
entry_p = tk.Entry(root)
entry_p.pack()

tk.Label(root, text="Rate %:").pack()
entry_r = tk.Entry(root)
entry_r.pack()

tk.Label(root, text="Years:").pack()
entry_t = tk.Entry(root)
entry_t.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

lbl_result = tk.Label(root, text="Interest: 0 | Total: 0", font=("Arial", 12, "bold"))
lbl_result.pack(pady=10)

root.mainloop()
