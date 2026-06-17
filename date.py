from datetime import date
import tkinter as tk


def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = date(year, month, day)
        today = date.today()

        if birth_date > today:
            result_label.config(text="Error: Future date.")
            return

        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            prev_month = today.month - 1 if today.month > 1 else 12
            prev_year = today.year if today.month > 1 else today.year - 1
            days_in_prev_month = (
                date(today.year, today.month, 1)
                - date(prev_year, prev_month, 1)
            ).days
            days += days_in_prev_month

        if months < 0:
            years -= 1
            months += 12

        result_label.config(text=f"{years}y, {months}m, {days}d")

    except ValueError:
        result_label.config(text="Error: Numbers only.")


root = tk.Tk()
root.title("Age Calc")
root.geometry("280x250")
root.config(bg="#f2f8f5")
root.resizable(False, False)

current_date_lbl = tk.Label(
    root,
    text=f"Today: {date.today().strftime('%d-%m-%Y')}",
    font=("Arial", 10, "bold"),
    bg="#e2f0e9",
    padx=5,
    pady=2,
)
current_date_lbl.pack(pady=5)

input_frame = tk.Frame(root, bg="#f2f8f5")
input_frame.pack(pady=5)

tk.Label(input_frame, text="Day:", font=("Arial", 10), bg="#f2f8f5").grid(
    row=0, column=0, padx=5, pady=2, sticky="e"
)
day_entry = tk.Entry(input_frame, width=6, font=("Arial", 10), justify="center")
day_entry.grid(row=0, column=1, pady=2)

tk.Label(input_frame, text="Month:", font=("Arial", 10), bg="#f2f8f5").grid(
    row=1, column=0, padx=5, pady=2, sticky="e"
)
month_entry = tk.Entry(
    input_frame, width=6, font=("Arial", 10), justify="center"
)
month_entry.grid(row=1, column=1, pady=2)

tk.Label(input_frame, text="Year:", font=("Arial", 10), bg="#f2f8f5").grid(
    row=2, column=0, padx=5, pady=2, sticky="e"
)
year_entry = tk.Entry(
    input_frame, width=6, font=("Arial", 10), justify="center"
)
year_entry.grid(row=2, column=1, pady=2)

calc_button = tk.Button(
    root,
    text="Calculate",
    font=("Arial", 10, "bold"),
    bg="#40916c",
    activebackground="#2d6a4f",
    command=calculate_age,
)
calc_button.pack(pady=5)

result_label = tk.Label(
    root,
    text="Enter details.",
    font=("Arial", 10, "italic"),
    bg="#f2f8f5",
    wraplength=250,
)
result_label.pack(pady=5)

root.mainloop()
