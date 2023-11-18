import socket

HOST, PORT = '127.0.0.1', 8001

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Enable the server to accept connections
server_socket.listen(1)
print(f"Listening on {HOST}:{PORT}")

while True:
    # Wait for a client to connect
    client_connection, client_address = server_socket.accept()
    print(f"Connected by {client_address}")

    # Receive the request
    request = client_connection.recv(1024).decode('utf-8')
    print(f"Request: {request}")

    # Send HTTP response
    response = "HTTP/1.1 200 OK\n\nHello, World!"
    client_connection.sendall(response.encode())

    # Close the connection
    client_connection.close()

# Close the server socket
server_socket.close()