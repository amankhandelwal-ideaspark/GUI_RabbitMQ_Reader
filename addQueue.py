from tkinter import *
from datasetup import DataSetup

class AddQueue:
    def __init__(self,r):
        self.root = r

    def saveInput(self,ip,port,host,user,pword,qn):
        con = DataSetup().getDbCon()
        cur = con.cursor()
        q = f"INSERT INTO queue_details(ipurl,port,virtual_host,uname,pword,queue_name) VALUES('{ip}','{port}','{host}','{user}','{pword}','{qn}')"
        cur.execute(q)
        print('Record received')

    def load(self):
        window = Toplevel(self.root)
        window.title('Add Queue')
        window.minsize(250, 150)
        label = Label(window,text='IP/URL').grid(row=2,column=1)
        label_port = Label(window,text='Port').grid(row=4,column=1)
        label_virtualhost = Label(window,text='Virtual Host').grid(row=6,column=1)
        label_user = Label(window,text='Username').grid(row=8,column=1)
        label_pass = Label(window,text='Password').grid(row=10,column=1)
        label_queuename = Label(window,text='Queue Name').grid(row=12,column=1)
        
        # taking queue IP/URL as input from user
        v_ip = StringVar()
        entry_ip = Entry(window,textvariable=v_ip,bd=5).grid(row=2,column=3)
        # Port number where the queue is open
        v_port = StringVar()
        entry_port = Entry(window,textvariable=v_port,bd=5).grid(row=4,column=3)
        # Virtual host if any used
        v_vh = StringVar()
        entry_vh = Entry(window,textvariable=v_vh,bd=5).grid(row=6,column=3)
        # username for authentication
        v_user = StringVar()
        entry_user = Entry(window,textvariable=v_user,bd=5).grid(row=8,column=3)
        # password for authentication
        v_pass = StringVar()
        entry_pass = Entry(window,textvariable=v_pass,bd=5).grid(row=10,column=3)
        # queue name
        v_qn = StringVar()
        entry_qn = Entry(window,textvariable=v_qn,bd=5).grid(row=12,column=3)
        Button(window, text='Save', command=lambda:self.saveInput(v_ip.get(),v_port.get(),v_vh.get(),v_user.get(),v_pass.get(),v_qn.get())).grid(row=16,column=3,pady=8)