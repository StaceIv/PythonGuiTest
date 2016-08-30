from tkinter import *

root = Tk()

photo = PhotoImage(file="Dice.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()