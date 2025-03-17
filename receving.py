import time
import zmq # type: ignore
import random

# Set up ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REP)
# Bind to address
# This is the address string. This is
#   where the socket will listen on the network port
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print(f"Received request from the client: {message.decode()}")

    if message.decode() == 'Q':  # Client asked server to quit
        break

    if message.decode() == "This is a message from CS361":
        print("Message verified: This is a message from CS361")

    # Generate a random number (simulating some 'work')
    num = random.randint(1, 5)
    time.sleep(3)  # Simulate work by sleeping for 3 seconds

    # Convert number to string to send back
    myNum = str(num)
    socket.send_string(myNum)

# Clean exit
context.destroy()


# while True:
#     message = socket.recv()
#     print(f"Received request from the client: {message.decode()}")

#     if len(message) > 0:
#         if message.decode() == 'Q': # Client asked server to quit
#             break

#         # This is where we can perform 'work' or
#         # tasks that we want our program to do.
#         # Generate a random number.
#         num = random.randint(1, 5)
#         # Make the program sleep for X seconds.
#         time.sleep(3)

#         # Alternatively, you can use a struct.
#         myNum = str(num)

#         # Send reply back to client
#         # @send_string(): sends a string
#         socket.send_string(myNum)
# # Make a clean exit.
# context.destroy()       