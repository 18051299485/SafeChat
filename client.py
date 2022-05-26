#coding:utf-8
import threading
from tkinter import *
import socket
import time


# 主窗口属性,循环主窗口
def setroot():
    #创建主窗口，设置主窗口属性
    global root,label,text

    root = Tk()
    root.geometry('800x600+1000+200')
    root.title('SafeChat')

    fram1=Frame(master=root,width=600,height=480)
    fram1.place(x=0,y=0)

    #消息显示区域
    label=Text(master=fram1,width=600,height=480)
    label.place(x=0,y=0)
    #滚动条
    bar=Scrollbar(master=label,orient='vertical')
    bar.place(x=580)
    bar.config(command=label.yview)#绑定text组件
    label.config(yscrollcommand=bar.set)


    #文本编辑区域
    fram2=Frame(master=root,width=600,height=120,bg='#D0D0D0')
    fram2.place(in_=fram1,rely=1)
    text=Text(master=fram2,width=600)
    text.place(x=0,y=0)


    #右侧布局
    fram3 = Frame(master=root, width=200, height=600, bg='#84AF9B')
    fram3.place(in_=fram1, relx=1)



    sendbutton=Button(master=fram2,text='发送',command=lambda:newmessage(message=text.get('0.0','end')))
    sendbutton.place(anchor='se',bordermode=OUTSIDE,x=600,y=120,width=50)





def client_socket():
    # 与服务端通信
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.connect(('127.0.0.1', 5000))

def newmessage(message):
    # 将消息推向serve
    s.sendall(message.encode('utf-8'))
    text.delete('0.0', END)
    print(message)

def getmessage():
    global data
    # 接受服务端广播消息
    while True:
        data = s.recv(1024)
        datas=eval(data.decode('utf-8'))
        data1=datas['ip']+'  '+datas['time']
        data2=str(datas['message'])
        label.insert('end',data1+'\n',)
        label.insert('end', data2 + '\n')



if __name__=='__main__':
    setroot()
    client_socket()
    task=threading.Thread(target=getmessage)
    task.start()

    root.mainloop()