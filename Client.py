import socket
import Encryption
# Client function to set up a connection to the server
def Client(host, port, message):
    
    client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_Socket.connect((host, port))
    print("Connected to server")

    client_Socket.sendall(message.encode('utf-8'))
    recv_Message = client_Socket.recv(1024).decode('utf-8')

    # Decrypts the message from the server 
    message = "".join(str(recv_Message))
    decrypt = Encryption.Encryption(message, "Encry")
    # Prints out the decrypted message
    print(f"Message recived: {decrypt}")

        
    # Closes the connection to the server
    client_Socket.close()
    print("Ending connection")

if __name__ == '__main__':
    
    # Variables to connect to server
    server_Ip = "127.0.0.1"
    server_Port = 1234
    # Take in user inputs then gets passed to be encrypted
    message = input("Enter your message: ")
    encrypt = Encryption.Encryption(message, "Encry")

    Client(server_Ip, server_Port, encrypt)