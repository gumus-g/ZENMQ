import zmq # type: ignore

# Set up ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
 # Connect to receiver
socket.connect("tcp://localhost:5555")

# Send the message "This is a message from CS361"
messageSend = "This is a message from CS361"
print(f"Sending a request: {messageSend}")
socket.send_string(messageSend)

# Get and print the reply from the server
response = socket.recv()
print(f"Server sent back: {response.decode()}")

# Tell the server to quit
socket.send_string("Q")