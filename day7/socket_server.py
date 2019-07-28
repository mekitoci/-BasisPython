import socket
import os
#伺服器端

server = socket.socket()

server.bind(("localhost",6969)) #綁定要監聽窗口
server.listen() #監聽
print("我要開始等電話了")
while True:
    conn, addr = server.accept()  # conn就是客戶端連過來而在服務器端為其生成的一個連接實例
    print(conn, addr)
    print("電話來了")
    while True:
        data = conn.recv(1024)
        print("recv:",data)
        conn.send(data.upper())
        if not data:
            print("client has lost...")
            break
        res = os.popen(data).read()
        conn.send(res)


server.close()

