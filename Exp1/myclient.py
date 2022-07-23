import socket
import ciphers
class Client:
    def __init__(self,host,port,message,cipher):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.connect((host,port))
            s.sendall(message.encode())
            data = s.recv(1024)
        print(f"Received: {data}")
        data = cipher.decrypt("in",data.decode())
        print(f"Final message: {data}")

if __name__=='__main__':
    cipher = ciphers.SubstitutionCipher()
    c = Client('127.0.0.1',6666,cipher.encrypt("four",input("Enter message: ")),cipher)

