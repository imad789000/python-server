
import socket
import threading
import sys

ip = socket.gethostbyname(socket.gethostname())
port = 8282
f = 'utf-8'

try:
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('blue-liveconsole11', port))

except:
    print("You are not connected to the wifi or the server is offline...")
    input("Press enter to exit...")
    quit()







def receive():
    try:
        while True:
            message = client.recv(1024).decode(f)
            if message == "name?":
                client.send(nickname.encode(f))
            else:
                if message != "usedname":
                    print(message)
                else:
                    print("this username is used")
                    print("Press enter to exit...")
                    input()
                    quit()
                    break
    except:
        print("Something went wrong ;(")
        input("Press enter to exit...")
        quit()


def send():
    print(f"press enter to join...")
    try:
        while True:
            
            message = f"{nickname}: {input()}" 
            client.send(message.encode(f))
    except:
        print("something wemt wrong ;(")
        input("Press enter to exit...")
        quit()


def pass_checker():
    while True:
        
        password = input("Type the password for the server: ")
        client.send(password.encode(f))
        wait = client.recv(1024).decode(f)
        if wait == "name?":
            global nickname
            nickname = input("Choose a nickname: ")
            thread = threading.Thread(target = receive)
            thread.start()

            thread1 = threading.Thread(target = send)
            thread1.start()
            break
            
        if wait == "wrong!":
            print("wrong password. Try again.")
            print("Exit the program and try again...")
            break

try:
    pass_checker()
except:
    print("main function error!")
    input("Press enter to exit...")
    quit()
