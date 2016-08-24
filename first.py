from tkinter import *

root = Tk()
#All new code between root = Tk() and root.mainloop()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="ButtonOne", fg="red")
button2 = Button(topFrame, text="ButtonTwo", fg="blue")
button3 = Button(topFrame, text="ButtonThree", fg="green")
button4 = Button(bottomFrame, text="ButtonFour", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()