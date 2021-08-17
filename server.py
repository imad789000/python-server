import socket
import threading
import sys

ip = socket.gethostbyname(socket.gethostname())
port = 5050
f = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))


Password = input("Please input a password for the server: ")

clients = []
names = []

def broadcast(message):
    try:
        for i in clients:
            i.send(str(message).encode(f))  
    except:
        print("client not connected")

def handle_client(connection, namede, name):
    while True:
        try:
            message = connection.recv(1024)
            print(message)
            broadcast(message.decode(f))
        except:
            index = names.index(name)
            clients.remove(connection)
            nname = names[index]
            names.remove(nname)
            broadcast(f"{namede} has left the chat.")
            connection.close()
            break


def start():
    try:
        server.listen()
        while True:
            try:
                print("Server is listening...")

                connection, addr = server.accept()

                password = connection.recv(1024).decode(f)
                print(password)

                if Password == password:
                    
                    connection.send("name?".encode(f))
                    name = connection.recv(1024)
                    if name in names:
                        connection.send("usedname".encode(f))
                        
                    else:
                        namede = name.decode(f)
                        names.append(name)
                        clients.append(connection)
                        print(f"{addr} has connected with nickname of '{namede}'")
                        broadcast(f"{namede} has connected!")
                        thread = threading.Thread(target = handle_client, args = (connection, namede, name))
                        thread.start()

                if password != Password:
                    connection.send("wrong!".encode(f)) 
            except:
                print("something went wrong")
    
            
            
        
        

            

        
    except:
        print(" Crashed XO")
            

        
start()