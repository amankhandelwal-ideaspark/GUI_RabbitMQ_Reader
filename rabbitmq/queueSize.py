import pika
from tkinter import messagebox

class QueueSize:
    def __init__(self,r):
        self.root = r
    
    def getSize(self,ip,port,vh,uname,qn,pword):
        print(ip,port,vh,uname,qn,pword)
        args = { "x-max-length": 100000,"x-overflow":'drop-head'}
        parameters = pika.URLParameters(f'amqp://{uname}:{pword}@{ip}:{port}/{vh}')
        
        try:
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            res = channel.queue_declare(queue=qn, durable=True, arguments=args)
            print(res)
            connection.close()
        except Exception as e:
            print(e)
            res = 'connection failed'
        messagebox.showinfo("Information",res)