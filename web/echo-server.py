# IPC进程通信——TCP协议
# 版本一——套接字服务端和客户端
"""
    TCP 服务端——监听端口，处理请求，分析TCP协议
"""
"""
    socket模块API
        socket()
        bind()
        listen()
        accept()
        connect()
        connect_ex()
        send()
        recv()
        close()
    还有socketserver模块等
"""
# echo-server.py

import socket
HOST = '' # 空字符串
#HOST = '127.0.0.1' # 标准自循环接口地址
PORT = 5000 # 监听端口必须大于1023
"""
	服务端启动步骤
 		socket()
 		bind()
 		listen()
 		accept()
"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#socket
    s.bind((HOST,PORT))		#bind 将网络接口HOST和本地端口PORT绑定
    s.listen()				#listen 
    conn, addr = s.accept() #accept 当客户端连接时，accept才会被调用，
    with conn:              #conn连接才会被创建
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)