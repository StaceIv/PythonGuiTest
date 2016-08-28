from tkinter import *


class StaceysButtons:
    def __init__(self, master): #master is root window.
                                #different names in here and below to be easy to differentiate
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("WOW, I don't understand how this works.")



root = Tk()
s = StaceysButtons(root)
root.mainloop()