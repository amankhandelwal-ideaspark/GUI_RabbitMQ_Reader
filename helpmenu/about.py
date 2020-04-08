from tkinter import *


class About:
    def __init__(self,r):
        self.root = r
    
    def load(self):
        filewin = Toplevel(self.root)
        button = Button(filewin, text="Do n")
        button.pack()
        #(self.root).mainloop()
        #(self.root).withdraw()