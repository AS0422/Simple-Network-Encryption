import socket
# Server function to host and allow connetions too
def Server(host, port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(3)
    print("Server is running")

    while True:
        client_Socket, client_Address = server.accept()
        # Recives any messages from client 
        print(f"Conneted: {client_Address}")
        
        message = client_Socket.recv(1024)
        print(f"Message: {message.decode('utf-8')}")
        # Sends any messages to client
        print(client_Socket.sendall(message))
        # Ends connection 
        client_Socket.close()
        print("End of connection")

if __name__ == '__main__':
    server_Ip = "127.0.0.1"
    server_Port = 1234
    Server(server_Ip, server_Port)