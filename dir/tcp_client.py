from socket import *
ADDR=("127.0.0.1",8888)
#默认就是tcp
tcp_socket=socket()
#连接服务器
tcp_socket.connect(ADDR)
#先发送再接收
msg=input(">>>")
tcp_socket.send(msg.encode())
data=tcp_socket.recv(1024)
print("From server:",data.decode())
#关闭客户端
tcp_socket.close()