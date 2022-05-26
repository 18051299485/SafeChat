import socket
import threading
import datetime

users=list()#存放所有用户
users_online=list()#存在所有在线用户

def socket_serve():
    global conns
    serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serve.bind(('127.0.0.1', 5000))
    serve.listen(5)
    conns = list()  # 存储所有sockets对象
    while True:
        conn, addr = serve.accept()  # 接受客户端链接
        conns.append(conn)
        task = threading.Thread(target=action, args=(conn,))
        task.start()
        # task.join()
        # conn.close()  # 关闭循环内部套接字

#接收客户端消息
def action(conn):
    global data,ip,time
    while True:
        data = conn.recv(1024)  # 接收数据
        ip=conn.getpeername()
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        broadcast()



#广播message
def broadcast():
    datas=dict(ip=ip[0],message=data.decode('utf-8'),time=time)
    for socket in conns:
        socket.sendall(str(datas).encode('utf-8'))
    print(datas)


if __name__ == '__main__':
    socket_serve()

