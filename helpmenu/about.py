from tkinter import *


class About:
    def __init__(self,r):
        self.root = r
    
    def load(self):
        window = Toplevel(self.root)
        Label(window,text='This queue reader was My First GUI based application.').grid(row=1,column=1)
        button = Button(window, text="Close").grid(row=2,column=2)
        #button.pack()
        #(self.root).mainloop()
        #(self.root).withdraw()