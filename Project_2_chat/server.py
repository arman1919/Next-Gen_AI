import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

clients = []

def handle_client(client_socket, client_address):
    try:
        # Welcome message when connecting the client
        client_socket.send("Welcome to the chat! Enter 'exit' to exit.".encode())

        while True:
            data = client_socket.recv(1024).decode()
            if data.lower() == 'exit':
                break

            # Sending messages to all clients
            for client in clients:
                if client != client_socket:
                    client.send(data.encode())
    except:
        pass
    finally:
        # Processing client disconnection
        clients.remove(client_socket)
        client_socket.close()
        print(f"Клиент {client_address} отключен.")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Сервер запущен на {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)

        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
