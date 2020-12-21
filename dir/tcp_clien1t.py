"""
重点代码
"""

from socket import *

# 声明服务端的地址
ADDR = ("127.0.0.1", 8888)
#默认就是tcp
tcp_socket = socket()
#连接服务器
tcp_socket.connect(ADDR)
#先发送再接收
while True:
    msg=input(">>>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    #结束退出
    # if msg==b"##":
        # break
    data = tcp_socket.recv(1024)
    print("From server:", data.decode())
#关闭
tcp_socket.close()
