"""
tcp服务端 循环示例1
重点代码 ！！！

* 同时只能处理一个客户端，必须一个
客户端退出才能连接下一个
* 如果tcp循环连续发送时要注意沾包问题
"""
from socket import *
from time import sleep
#创建套接字,默认就是tcp
tcp_socket=socket(AF_INET,SOCK_STREAM)
#绑定地址
tcp_socket.bind(("0.0.0.0",8888))
#设置监听
tcp_socket.listen(5)
#循环连接客户端
while True:
    print("等待客户端连接:")
    connfd,addr=tcp_socket.accept()
    print("连接:",addr)
    #先发后收
    while True:
        data=connfd.recv(1024)
        if not data:
            break

        print("Recv:",data.decode())
        connfd.send(b"ok##")
        sleep(0.2)
    connfd.close()
#关闭套接字
tcp_socket.close()