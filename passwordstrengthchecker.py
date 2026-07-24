from tkinter import *
root = Tk()
window = Tk()
window.title("PASWORD strENGTH Cheker app")
label = Label(text="PASSWORD STRENGTH CHECKER",fg='pink',bg='blue')
text = Text(fg='Black',bg='White')
def checkstrength():
    p=text.get()
    length=len(p)
    if text<=5:
        result.config(text='weak',bg='red')
    if text<=8:
        result.config(text='medium',bg='red')
    if text<=12:
        result.config(text='strong',bg='red')        

button= Button(text='check',bg='red')    
label.place(x=230,y=50)
text.place(x=200,y=80)
button.place(x=240,y=120)
result=Label
result.place(x=230,y=250)
root.mainloop()
    