import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    try:
        while True:
            data = client_socket.recv(1024).decode()
            print(data)
    except:
        pass

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        client_socket.send(message.encode())
        if message.lower() == 'exit':
            break

    client_socket.close()

if __name__ == "__main__":
    main()
