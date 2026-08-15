import socket
import threading

HOST = "localhost"
PORT = 5000


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")

            if not message:
                print("\nServer disconnected.")
                break

            print(f"\n{message}")
            print("You: ", end="", flush=True)

        except (ConnectionResetError, ConnectionAbortedError, OSError):
            print("\nDisconnected from server.")
            break


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect to the server.")
        print("Make sure server.py is running first.")
        return

    print("Connected to the chat server.")

    username_prompt = client.recv(1024).decode("utf-8")
    print(username_prompt, end="")

    username = input()
    client.send(username.encode("utf-8"))

    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client,)
    )

    receive_thread.daemon = True
    receive_thread.start()

    print("\nYou can now start chatting.")
    print("Type /quit to leave the chat.\n")

    try:
        while True:
            message = input("You: ")

            if not message.strip():
                continue

            client.send(message.encode("utf-8"))

            if message.lower() == "/quit":
                break

    except (KeyboardInterrupt, EOFError):
        try:
            client.send("/quit".encode("utf-8"))
        except:
            pass

    finally:
        client.close()
        print("Disconnected from chat.")


if __name__ == "__main__":
    start_client()