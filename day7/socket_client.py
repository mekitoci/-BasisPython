import socket
#客戶端
client = socket.socket() #聲明socket類型,同時生成socket連接對象
client.connect(('localhost',6969))

while True:
    msg = input("＞＞").strip()

    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    print(data.decode())

client.close()
