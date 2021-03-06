"""
IO并发模型 基于epoll方法 tcp
重点代码!!!
"""
from socket import *
from select import *

HOST = "0.0.0.0"
PORT = 2222
ADDR = (HOST, PORT)
# 创建tcp套接字连接客户端,处理请求
tcp_socket = socket()
tcp_socket.bind(ADDR)
tcp_socket.listen(5)
# 设置为非阻塞IO
tcp_socket.setblocking(False)

ep = epoll()  # 创建epoll对象
# 设置监控
ep.register(tcp_socket, EPOLLIN | EPOLLERR)
# 查找字典 时刻与关注的IO保持一致
map = {tcp_socket.fileno(): tcp_socket}
# 循环的监控发生的IO事件
while True:
    events = ep.poll()
    # 遍历就绪的IO对象  events--->[(fd,event)]
    for fd, event in events:
        # 分情况讨论
        if fd is tcp_socket.fileno():  # 监听套接字
            # 处理客户端连接
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            # 添加客户端连接套接字到监控列表
            connfd.setblocking(False)
            map[connfd.fileno()] = connfd  # 维护字典
            ep.register(connfd, EPOLLIN)
        else:
            # 处理一个客户端的信息
            data = map[fd].recv(1024)
            if not data:
                ep.unregister(fd)
                map[fd].close()
                del map[fd]

                continue
            print(data.decode())
            map[fd].send(b"OK")
