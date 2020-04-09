from tkinter import *
from datasetup import DataSetup
from helpmenu.about import About
from addQueue import AddQueue
from rabbitmq.queueSize import QueueSize

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
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.quit)

menubar.add_cascade(label = "File", menu = filemenu)

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
#label = Label(root,textvariable = var).grid(row=2,column=2)
var.set("sample text")


con = db.getDbCon()
cur = con.cursor()
cur.execute('select _rowid_,ipurl,port,virtual_host,uname,queue_name,pword from queue_details')
rows = cur.fetchall()

rn = 2
index = 0
for row in rows:
    sn = row[0]
    ip = row[1]
    port = row[2]
    vh = row[3]
    uname = row[4]
    qn = row[5]
    pword = row[6]
    Label(root,text=sn).grid(row=rn,column=2)
    Label(root,text=ip).grid(row=rn,column=3)
    Label(root,text=port).grid(row=rn,column=4)
    Label(root,text=vh).grid(row=rn,column=6)
    Label(root,text=uname).grid(row=rn,column=8)
    Label(root,text=qn).grid(row=rn,column=10)
    Button(root,text='View size',command=lambda:QueueSize(root).getSize(rows[index][1],rows[index][2],rows[index][3],rows[index][4],rows[index][5],rows[index][6])).grid(row=rn,column=12)
    rn = rn + 1
    index = index + 1

print('rows fetched')
root.config(menu=menubar)
root.minsize(450, 250)
root.title('RabbitMQ Reader')
root.mainloop()