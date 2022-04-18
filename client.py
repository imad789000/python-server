import socket, threading

ip = input("enter an ip: ")

HOST = ip  # The server's hostname or IP address
PORT = 6060  # The port used by the server

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))
    
def sending():
    while True:
        message = input()
        soc.send(message.encode("utf-8"))

def recve():
    while True:
        msg = soc.recv(1024).decode("utf-8")
        print(msg)


thread = threading.Thread(target=sending).start()
recve()

