import socket
import ciphers

substitutionCipher = ciphers.SubstitutionCipher()

HOST = '127.0.0.1'
PORT =  6666

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data = data.decode()
            print(f"Received: {data}")
            data = substitutionCipher.decrypt("four",data)
            print(f"Message: {data}")
            data = substitutionCipher.encrypt("four",data)
            print(f"Sent: {data}")
            conn.sendall(data.encode())