# Author: Jackie Truong
# Course: CS325 - Analysis of Algorithms
# Assignment: Microservice A (make a microservice for another teammate)
# Description: Receives username and password as a dictionary and searches
#              through credentials file for a matching account.

import os
import zmq
import json
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:----") # INSERT HOST HERE

while True:
    #  Wait for request from client
    print("Waiting for request...")
    login_info = socket.recv_json() # a dictionary

    # Received request

    print(f'Received request: {login_info}')
    time.sleep(1)

    # Searching for login match
    login_user = login_info["username"]
    login_pass = login_info["password"]

    result = False
    if os.path.exists("credentials.txt"):   # You change the name of text file, if you prefer
        try:
            print("Searching file...")
            time.sleep(1)
            with open("credentials.txt", "r") as f:
                account_data = json.load(f)
                for account in account_data:
                    if login_user == account["username"] and login_pass == account["password"]:
                        result = True
                        print("-- Account match found!")
                if result == False:
                    print("-- Account does not exist")
        except:
            print("-- No accounts stored")
    else:
        print("File does not exist")
    time.sleep(1)

    # Send response - True if account exists, False if it does not
    print(f'Responding with: {result}\n')
    socket.send_pyobj(result)   # Send boolean as response