# Chat Application

## Internship Project – Real-Time Chat Application

### Project Overview

The **Chat Application** is a real-time messaging application developed using **Python sockets and threading**. The application allows two users to communicate with each other through a server-client architecture.

The beginner version provides a command-line interface where multiple clients can connect to the server and exchange messages in real time. Messages include timestamps and usernames, and the application handles client disconnections gracefully.

This project demonstrates fundamental concepts of:

* Python networking
* Socket programming
* Client-server architecture
* Multithreading
* Real-time communication
* Exception handling
* User input/output
* Graceful connection management

---

## Objectives

The main objectives of this project are:

1. Build a server that listens for incoming client connections.
2. Build a client that connects to the server.
3. Enable real-time, bidirectional communication.
4. Support two users chatting simultaneously.
5. Display messages with timestamps.
6. Display usernames along with messages.
7. Handle client disconnections gracefully.
8. Run both the server and clients on the same computer using `localhost`.

---

## Technologies Used

| Technology  | Purpose                                  |
| ----------- | ---------------------------------------- |
| Python      | Main programming language                |
| `socket`    | Network communication                    |
| `threading` | Handle multiple clients simultaneously   |
| `datetime`  | Generate message timestamps              |
| `localhost` | Run the application on a single computer |

### Python Libraries

The beginner version primarily uses Python's built-in libraries:

```text
socket
threading
datetime
```

No external Python packages are required for the beginner version.

---

# Project Structure

Create a project folder with the following structure:

```text
chat_application/
│
├── server.py
├── client.py
└── README.md
```

### File Description

#### `server.py`

The server program:

* Creates a socket.
* Binds the socket to `localhost`.
* Listens for incoming connections.
* Accepts clients.
* Creates a separate thread for each client.
* Receives and broadcasts messages.
* Handles client disconnections.

#### `client.py`

The client program:

* Connects to the server.
* Asks the user for a username.
* Sends messages to the server.
* Receives messages from other users.
* Uses a separate thread to receive messages while allowing the user to type.

#### `README.md`

This file contains:

* Project information
* Installation instructions
* Usage instructions
* Features
* Technology stack
* Testing information
* Security information
* Future improvements

---

# How the Application Works

The application follows a basic **client-server architecture**.

```text
             ┌──────────────────┐
             │      SERVER      │
             │                  │
             │   localhost      │
             │   Port: 5555     │
             └────────┬─────────┘
                      │
             ┌────────┴─────────┐
             │                  │
             ▼                  ▼
      ┌─────────────┐    ┌─────────────┐
      │   Client 1  │    │   Client 2  │
      │    Alice    │    │     Bob     │
      └─────────────┘    └─────────────┘
```

The server acts as the central communication point.

When Alice sends:

```text
Hello Bob!
```

The server receives the message and sends it to Bob.

The message is displayed as:

```text
[14:35] Alice: Hello Bob!
```

---

# Features

## Beginner Tier

* [x] Server script that listens for incoming client connections
* [x] Client script that connects to the server
* [x] Real-time bidirectional message exchange
* [x] Timestamp displayed with messages
* [x] Username displayed with messages
* [x] Graceful disconnection handling
* [x] Runs on the same computer using `localhost`
* [x] Supports multiple connected clients through threading

---

# Installation

## Step 1 – Install Python

Make sure Python is installed on your computer.

Check the installed Python version using:

```bash
python --version
```

or:

```bash
python3 --version
```

Example:

```text
Python 3.13.9
```

---

## Step 2 – Create the Project Folder

Create a folder named:

```text
chat_application
```

Open the folder in your code editor.

---

## Step 3 – Create the Python Files

Create two Python files:

```text
server.py
client.py
```

The final folder should look like:

```text
chat_application/
│
├── server.py
├── client.py
└── README.md
```

---

# Running the Application

The server must be started before the clients.

## Step 1 – Open Terminal

Open Command Prompt or the terminal in your project folder.

Example:

```bash
cd path\to\chat_application
```

---

## Step 2 – Start the Server

Run:

```bash
python server.py
```

The server should display something similar to:

```text
Server started on localhost:5555
Waiting for connections...
```

Keep this terminal open.

---

## Step 3 – Start Client 1

Open another terminal window.

Run:

```bash
python client.py
```

Enter a username:

```text
Enter your username: Alice
```

---

## Step 4 – Start Client 2

Open a third terminal window.

Run:

```bash
python client.py
```

Enter another username:

```text
Enter your username: Bob
```

Now Alice and Bob can communicate.

---

# Example Conversation

### Alice's Terminal

```text
Enter your username: Alice

[14:35] Bob: Hello Alice!
Hello Bob!
```

### Bob's Terminal

```text
Enter your username: Bob

Hello Alice!
[14:35] Alice: Hello Bob!
```

The timestamp is generated automatically.

---

# Server Responsibilities

The server is responsible for managing the communication between clients.

The main operations are:

### 1. Create Socket

```python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### 2. Bind Socket

```python
server_socket.bind(("localhost", 5555))
```

### 3. Listen for Connections

```python
server_socket.listen()
```

### 4. Accept Clients

```python
client_socket, address = server_socket.accept()
```

### 5. Create Threads

Each connected client can be handled using a separate thread:

```python
thread = threading.Thread(target=handle_client, args=(client_socket,))
thread.start()
```

This allows multiple clients to communicate without blocking the server.

---

# Client Responsibilities

The client connects to the server using:

```python
client_socket.connect(("localhost", 5555))
```

The client performs two major operations:

### Sending Messages

The user types a message and the client sends it to the server.

### Receiving Messages

A separate thread continuously waits for messages from the server.

This is important because the user should be able to type while receiving messages from another client.

---

# Why Threading Is Used

Without threading, the server may only be able to handle one client at a time.

For example:

```text
Client 1 connects
       ↓
Server waits for Client 1
       ↓
Client 2 cannot communicate properly
```

With threading:

```text
                 SERVER
                   │
        ┌──────────┴──────────┐
        │                     │
     Thread 1              Thread 2
        │                     │
     Client 1              Client 2
```

Each client gets its own thread.

This allows the application to support simultaneous communication.

---

# Timestamp Format

Messages are displayed using the following format:

```text
[HH:MM] Username: Message
```

For example:

```text
[14:35] Alice: Hello!
```

The timestamp can be generated using Python's `datetime` module.

Example:

```python
from datetime import datetime

timestamp = datetime.now().strftime("%H:%M")
```

---

# Graceful Disconnection

The application handles situations where a user closes the client or disconnects from the server.

For example:

```text
[14:40] Alice has disconnected.
```

The other connected users are notified about the disconnection.

The server also removes disconnected clients from its active client list.

---

# Testing

The application should be tested using multiple terminal windows.

## Test 1 – Server Startup

Expected result:

```text
Server started on localhost:5555
Waiting for connections...
```

## Test 2 – Client Connection

Start a client.

Expected result:

```text
Connected to server.
Enter your username:
```

## Test 3 – Two Clients

Start two clients.

Expected result:

```text
Alice connected.
Bob connected.
```

## Test 4 – Message Exchange

Alice sends:

```text
Hello Bob!
```

Bob should receive:

```text
[14:35] Alice: Hello Bob!
```

## Test 5 – Disconnection

Close Alice's client.

Bob should receive a notification similar to:

```text
[14:40] Alice has disconnected.
```

---

# Common Errors and Solutions

## Error 1 – Connection Refused

Example:

```text
ConnectionRefusedError
```

### Solution

Make sure the server is running before starting the client.

Correct order:

```text
1. Start server.py
2. Start client.py
3. Start another client.py
```

---

## Error 2 – Address Already in Use

Example:

```text
OSError: [WinError 10048]
```

### Solution

The port may already be occupied by another server process.

Stop the previous server and try again.

You can also use another port, such as:

```text
5556
```

Make sure the same port is used in both `server.py` and `client.py`.

---

## Error 3 – Python Is Not Recognized

Example:

```text
'python' is not recognized as an internal or external command
```

### Solution

Make sure Python is installed and added to the system PATH.

Try:

```bash
py --version
```

If that works, run the application using:

```bash
py server.py
```

and:

```bash
py client.py
```

---

# Security Considerations

This beginner application is designed for **learning purposes**.

Messages are transmitted through a normal TCP socket connection.

The beginner version does **not** provide:

* End-to-end encryption
* User authentication
* Password protection
* Secure password storage
* TLS/SSL encryption
* Database-backed message history

Therefore, this application should **not be used to transmit sensitive or confidential information**.

The project demonstrates networking concepts rather than production-level security.

---

# Advanced Version – Future Improvements

The application can be extended into a complete GUI-based messaging platform.

Possible improvements include:

* [ ] GUI chat window using Tkinter
* [ ] User registration
* [ ] User login
* [ ] SQLite database
* [ ] Password hashing
* [ ] Multiple chat rooms
* [ ] Create and join rooms
* [ ] Message history
* [ ] Desktop notifications
* [ ] Emoji support
* [ ] Online/offline user status
* [ ] User profile
* [ ] File sharing
* [ ] Secure communication using TLS
* [ ] End-to-end encryption awareness
* [ ] Web-based interface using Flask-SocketIO

---

# Advanced Technology Stack

The advanced version can use:

```text
Python
│
├── socket / asyncio
├── Flask-SocketIO
├── Tkinter
├── SQLite
└── threading
```

### SQLite

SQLite can be used to store:

```text
Users
Rooms
Messages
```

Example database structure:

```text
users
------------------
id
username
password_hash

rooms
------------------
id
room_name

messages
------------------
id
room_id
username
message
timestamp
```

---

# Message History

When a user joins a room, previous messages can be retrieved from the database.

Example:

```text
--- General Room ---

[14:30] Alice: Hello!
[14:31] Bob: Hi Alice!
[14:32] Alice: How are you?
```

New messages can then continue below the previous history.

---

# Emoji Support

The advanced application can convert common emoji shortcodes into Unicode characters.

For example:

```text
Hello :smile:
```

can be displayed as:

```text
Hello 😄
```

Common examples include:

```text
:smile:  → 😄
:heart:  → ❤️
:thumbsup: → 👍
:fire: → 🔥
```

---

# Security Transparency

The README must clearly explain how messages are stored and transmitted.

For the beginner version:

```text
Messages are transmitted through TCP sockets.
Messages are not end-to-end encrypted.
No permanent message history is stored by default.
```

For an advanced SQLite implementation:

```text
Messages may be stored in an SQLite database.
Passwords must be stored as secure password hashes rather than plain text.
Database access should be protected.
Network communication should use secure encryption such as TLS when handling sensitive information.
```

---

# Learning Outcomes

After completing this project, the following concepts should be understood:

### Python

* Functions
* Classes
* Exception handling
* Modules
* Lists and dictionaries
* String formatting

### Networking

* IP addresses
* Ports
* TCP communication
* Sockets
* Client-server architecture
* Sending and receiving data

### Concurrency

* Threads
* Multiple clients
* Simultaneous communication
* Thread-safe handling of shared data

### Software Development

* Project structure
* Testing
* Debugging
* Documentation
* Security awareness

---

# Self-Sourcing and References

The following resources can be used to understand the networking concepts used in this project.

### Python Socket Documentation

Official Python documentation:

https://docs.python.org/3/library/socket.html

### Python Threading Documentation

Official Python documentation:

https://docs.python.org/3/library/threading.html

### Recommended YouTube Searches

Search YouTube for:

```text
Python socket programming tutorial beginners
```

For the beginner chat application:

```text
Python chat app socket threading tutorial
```

For the advanced GUI/web application:

```text
Flask SocketIO real-time chat tutorial
```

or:

```text
Python tkinter chat application tutorial
```

---

# Project Demonstration

For the internship demonstration, show the following steps:

### Step 1

Open the project folder.

### Step 2

Open three terminals.

### Step 3

Run:

```bash
python server.py
```

### Step 4

Run Client 1:

```bash
python client.py
```

Enter:

```text
Alice
```

### Step 5

Run Client 2:

```bash
python client.py
```

Enter:

```text
Bob
```

### Step 6

Send messages between Alice and Bob.

Example:

```text
Alice: Hello Bob!
Bob: Hello Alice!
Alice: This is my Python chat application.
Bob: It works!
```

### Step 7

Close one client and demonstrate the disconnection notification.

---

# Beginner Feature Checklist

* [x] Server script created
* [x] Client script created
* [x] Server listens for connections
* [x] Client connects to server
* [x] Two-way communication implemented
* [x] Timestamp added to messages
* [x] Username displayed
* [x] Threading used
* [x] Graceful disconnection implemented
* [x] Runs using `localhost`
* [x] Project documented using README.md

---

# Conclusion

The **Chat Application** demonstrates how Python can be used to build a real-time communication system using sockets and threading.

The beginner version provides the fundamental networking functionality required for two users to exchange messages through a central server. The project can later be expanded with a graphical interface, authentication, chat rooms, SQLite message history, notifications, emoji support, and secure communication.

This project provides practical experience with **Python networking, socket programming, threading, client-server architecture, error handling, testing, and software documentation**.

---

## Internship Submission

**Project Name:** Chat Application

**Project Type:** Python Networking Project

**Level:** Beginner Tier

**Programming Language:** Python

**Main Libraries:** `socket`, `threading`, `datetime`

**Interface:** Command Line

**Communication:** TCP Socket

**Host:** `localhost`

**Purpose:** Educational / Internship Project
