from tkinter import *

class AddQueue:
    def __init__(self,r):
        self.root = r

    def load(self):
        window = Toplevel(self.root)
        window.title('Add Queue')
        window.minsize(250, 150)
        label = Label(window,text='IP/URL').grid(row=2,column=1)
        label_port = Label(window,text='Port').grid(row=4,column=1)
        label_virtualhost = Label(window,text='Virtual Host').grid(row=6,column=1)
        label_user = Label(window,text='Username').grid(row=8,column=1)
        label_pass = Label(window,text='Password').grid(row=10,column=1)
        
        entry_ip = Entry(window,bd=5).grid(row=2,column=3)
        entry_port = Entry(window,bd=5).grid(row=4,column=3)
        entry_vh = Entry(window,bd=5).grid(row=6,column=3)
        entry_user = Entry(window,bd=5).grid(row=8,column=3)
        entry_pass = Entry(window,bd=5).grid(row=10,column=3)