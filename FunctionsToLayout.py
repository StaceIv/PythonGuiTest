from tkinter import *

root = Tk()

def printName(event):
    print("Hello my name is Stacey")

button_1 = Button(root, text="PrintName")
button_1.bind("<Button-1>", printName) #2 parameters: what event occurs, and what happens when even occurs
button_1.pack()

root.mainloop()