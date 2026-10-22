Aim
To implement a simple client–server communication model using sockets or gRPC for exchanging
messages between distributed nodes.
Learning Objectives
After completing this practical, students should be able to:
● Explain the client–server communication model.
● Establish communication between two distributed processes.
● Send and receive messages using sockets or gRPC.
● Handle connection and communication errors.
Background
In the client–server model, the server waits for requests from clients. The client initiates communication
by connecting to the server and sending a request. The server processes the request and returns a
response.
Typical communication steps are:
1. Server creates a socket.
2. Server binds the socket to an IP address and port.
3. Server listens for client requests.
4. Client creates a socket and connects to the server.
5. Client sends a message or request.
6. Server receives and processes the message.
7. Server sends a response.
8. Both sides close the connection.
Requirements
● Implement a server program.
● Implement a client program.
● Exchange at least three messages.
● Display messages sent and received by both sides.
● Implement graceful connection termination.
● Handle the case in which the server is unavailable.