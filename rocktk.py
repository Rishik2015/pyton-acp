import tkinter as tk
import random

score = 0

def play(user):
    global score
    comp = random.choice(["Rock", "Paper", "Scissors"])
    
    if user == comp:
        res = "Tie!"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissors" and comp == "Paper"):
        res = "Win!"
        score += 1
    else:
        res = "Lose!"
        score -= 1
        
    lbl.config(text=f"{user} vs {comp}\n{res}\nScore: {score}")

root = tk.Tk()
root.geometry("200x120")

lbl = tk.Label(root, text="Play!", font=("Arial", 12))
lbl.pack(pady=5)

for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(root, text=choice, command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=5, expand=True)

root.mainloop()

