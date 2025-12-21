#!/usr/bin/python3
"""
Module for a simple client-server application using JSON serialization
"""
import socket
import json


def start_server():
    """
    Starts a server that listens for a connection, receives a JSON 
    serialized dictionary, and prints it.
    """
    host = 'localhost'
    port = 65432

    try:
        # Create a socket (AF_INET for IPv4, SOCK_STREAM for TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Bind the socket to the address and port
            s.bind((host, port))
            # Listen for incoming connections
            s.listen()
            
            conn, addr = s.accept()
            with conn:
                # Receive the data (1024 bytes buffer)
                data = conn.recv(1024)
                if data:
                    # Deserialize JSON data back to a dictionary
                    received_dict = json.loads(data.decode('utf-8'))
                    print(f"Received Dictionary from Client:")
                    print(received_dict)
    except Exception as e:
        print(f"Server error: {e}")


def send_data(data_dict):
    """
    Connects to the server and sends a serialized dictionary.
    """
    host = 'localhost'
    port = 65432

    try:
        # Create a socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((host, port))
            # Serialize the dictionary to a JSON string and encode to bytes
            serialized_data = json.dumps(data_dict).encode('utf-8')
            # Send the data
            s.sendall(serialized_data)
    except ConnectionRefusedError:
        print("Connection failed: Server is not responding.")
    except Exception as e:
        print(f"Client error: {e}")
