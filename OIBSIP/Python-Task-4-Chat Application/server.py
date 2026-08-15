import socket
import threading
from datetime import datetime

HOST = "localhost"
PORT = 5000

clients = {}
lock = threading.Lock()


def timestamp():
    return datetime.now().strftime("%H:%M")


def broadcast(message, sender=None):
    with lock:
        disconnected = []

        for client, username in clients.items():
            if client != sender:
                try:
                    client.send(message.encode("utf-8"))
                except:
                    disconnected.append(client)

        for client in disconnected:
            clients.pop(client, None)
            client.close()


def handle_client(client, address):
    try:
        client.send("Enter your username: ".encode("utf-8"))
        username = client.recv(1024).decode("utf-8").strip()

        if not username:
            username = f"User-{address[1]}"

        with lock:
            clients[client] = username

        print(f"{username} connected from {address}")

        join_message = f"[{timestamp()}] {username} joined the chat."
        print(join_message)
        broadcast(join_message, client)

        while True:
            data = client.recv(1024)

            if not data:
                break

            message = data.decode("utf-8").strip()

            if message.lower() == "/quit":
                break

            formatted_message = f"[{timestamp()}] {username}: {message}"

            print(formatted_message)
            broadcast(formatted_message, client)

    except ConnectionResetError:
        pass

    finally:
        with lock:
            username = clients.pop(client, None)

        client.close()

        if username:
            leave_message = f"[{timestamp()}] {username} left the chat."
            print(leave_message)
            broadcast(leave_message)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print("=" * 40)
    print("Chat Server Started")
    print(f"Listening on {HOST}:{PORT}")
    print("Waiting for clients...")
    print("=" * 40)

    while True:
        client, address = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(client, address)
        )

        thread.daemon = True
        thread.start()


if __name__ == "__main__":
    start_server()