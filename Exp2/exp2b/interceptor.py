import os
import socket
from time import sleep
import ciphers

class Interceptor:
    def __init__(self,host,port,cipher):
        os.system("clear")
        print("Interceptor is running...")
        print(host)
        print("Interceptor is collecting data....")
        self.getData(host,port,cipher)

    def getData(self,host,port,cipher):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            data = ""
            s.bind((host,port))
            s.listen()
            conn,addr = s.accept()
            newMessage = input("Enter message you want to send:")
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    data = data.decode()
                    print(f"Received: {data}")
                    data = cipher.decrypt("four",data)
                    print(f"Message: {data}")
                    data = cipher.encrypt("four",newMessage)
                    print(f"Sent: {data}")
                    break
        self.sendServer('127.0.0.1',6666,data)

    def sendServer(self,host,port,message):
        print("Interceptor is sending data to the server...")
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.connect((host,port))
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Data:{data.decode()}")


if __name__=="__main__":
    Intercept = Interceptor("",1234,ciphers.SubstitutionCipher())
