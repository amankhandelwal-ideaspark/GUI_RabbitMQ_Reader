from tkinter import *
from datasetup import DataSetup
from helpmenu.about import About
from addQueue import AddQueue

root = Tk()

db = DataSetup()
about = About(root)

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()



menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = AddQueue(root).load)
filemenu.add_command(label = "Open", command = donothing)
filemenu.add_command(label = "Save", command = donothing)
filemenu.add_command(label = "Save as...", command = donothing)
filemenu.add_command(label = "Close", command = donothing)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.quit)

menubar.add_cascade(label = "File", menu = filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Undo", command = donothing)
editmenu.add_separator()
editmenu.add_command(label = "Cut", command = donothing)
editmenu.add_command(label = "Copy", command = donothing)
editmenu.add_command(label = "Paste", command = donothing)
editmenu.add_command(label = "Delete", command = donothing)
editmenu.add_command(label = "Select All", command = donothing)

menubar.add_cascade(label = "Edit", menu = editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Help Index", command = donothing)
helpmenu.add_command(label = "About", command = about.load)

menubar.add_cascade(label = "Help", menu = helpmenu)


# opening window

var = StringVar()
label = Label(root,textvariable = var,width=15).grid(row=1,column=2)
var.set("S.No.")
Label(root,text='IP',width=15).grid(row=1,column=3)
Label(root,text='Port',width=15).grid(row=1,column=4)
Label(root,text='Virtual Host',width=15).grid(row=1,column=6)
Label(root,text='Username',width=15).grid(row=1,column=8)
Label(root,text='Queue Name',width=15).grid(row=1,column=10)
Label(root,text='Actions',width=15).grid(row=1,column=12)

var = StringVar()
label = Label(root,textvariable = var).grid(row=2,column=2)
var.set("sample text")

root.config(menu=menubar)
root.minsize(450, 250)
root.title('RabbitMQ Reader')
root.mainloop()