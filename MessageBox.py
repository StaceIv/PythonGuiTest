from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Monkeys live long.")

answer = tkinter.messagebox.askquestion("Window Title", "This is the question")

if answer == 'yes':
    print('YES')

root.mainloop()