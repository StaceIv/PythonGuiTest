from tkinter import *

root = Tk()

def leftClick(event):
    print("LEFT")

def middleClick(event): #middleClick = click the scroll wheel
    print("MIDDLE")

def rightClick(event):
    print("RIGHT")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()