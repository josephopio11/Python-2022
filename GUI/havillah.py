from tkinter import *

window = Tk()
window.title("Havillah from Mpongo Clan")

lbl1 = Label(window, text="Welcome to my first GUI")
lbl1.grid(column=0, row=0)

lbl2 = Label(window, text="I come from Kinanira", font=("Arial", 40))
lbl2.grid(column=0, row=1)

btn = Button(window, text="Click Here")
btn.grid(column=0, row=2)
# Write a GUI having a letter written to me (the teacher)

window.mainloop()
