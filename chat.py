
from tkinter import *
import time



# 主窗口属性,循环主窗口
def setroot():
    #创建主窗口，设置主窗口属性
    global root
    root = Tk()
    root.geometry('800x500+1000+200')
    root.title('SafeChat')

# 页面布局
#登陆页面布局
def login_frame():

    frame_login=Frame(root,bg='#2C3E50')
    frame_login.pack(fill='both',expand=True)

    frame_login2=Frame(frame_login,bg='#D24D57',width=200,height=100)
    frame_login2.pack(anchor='center',expand=1,side='top')


    #
    # label_account=Label(frame_login2,text="账号")
    # label_account.pack()
    # label_password=Label(frame_login2,text="密码")
    # label_password.pack()



#注册账号
# def register():





if __name__=='__main__':
    setroot()
    login_frame()
    root.mainloop()
