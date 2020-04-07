from tkinter import *


class About:
    def __init__(self):
        self.root = Tk()
    
    def load(self):
        t = Text(self.root)
        t.insert(INSERT, 'Sample about text')
        t.pack()
        (self.root).mainloop()