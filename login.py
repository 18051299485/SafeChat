
from tkinter import *
import time



# 主窗口属性,循环主窗口
def setroot():
    #创建主窗口，设置主窗口属性
    global root
    root = Tk()
    root.geometry('800x600+1000+200')
    root.title('SafeChat')

# 页面布局
#登陆页面布局
def login_frame():

    frame_login=Frame(root,bg='#FC9D99')
    frame_login.pack(fill='both',expand=True)

    frame_login2=Frame(frame_login,width=250,height=170)
    frame_login2.pack(anchor='center',expand=1,side='top')

    label_account=Label(master=frame_login2,text="账号")
    label_account.place(x=25,y=40)
    entry_account=Entry()
    entry_account.place(in_=label_account,relx=1.5)


    label_password=Label(master=frame_login2,text="密码")
    label_password.place(in_=label_account,rely=2,bordermode=OUTSIDE)

    entry_password=Entry()
    entry_password.place(in_=label_password,relx=1.5)

    # 使用lambda为button传参
    login_button=Button(master=frame_login2,text="登陆",width=10,command=lambda:register(x=entry_account.get(),y=entry_password.get()))
    login_button.place(x=90,y=130)



# 注册账号

def register(x,y):
    with open("info.txt",mode="a") as file:
        file.write(x+'|')
        file.write(y+'\n')
    print(x,y)


if __name__=='__main__':
    setroot()
    login_frame()
    root.mainloop()