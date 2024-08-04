# Author: Jackie Truong
# Course: CS361 - Software Engineering
# Assignment: Microservice A (make a microservice for another teammate)
# Description: Client server for login service

import zmq

def login():
    # Connecting to log in server
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:----")  # INSERT HOST HERE

    # Get user input
    user_input = input("Enter Username: ")
    password_input = input("Enter Password: ")
    login_info = {"username": user_input,
                  "password": password_input}

    # Sends request
    socket.send_json(login_info)

    # Receives response
    login_status = socket.recv_pyobj()

    if login_status == True:
        print("[ Account exists ]")
    else:
        print("[ Account does not exist ]")

    print("")
    print("")
    print("")

if __name__ == "__main__":
    context = zmq.Context()  # Set up ZMQ
    login()
    context.term()  # Closes out ZMQ


