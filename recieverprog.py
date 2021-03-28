import socket
from utilities import *
s = socket.socket()
host = "127.0.0.1"
port = 60003
try:
    s.connect((host, port))
    print(f"Connection to {host} has been established")
    data = s.recv(1024)
    codeword =data.decode()
    #codeword = "101011111"
    print("The recieved codeword is ", codeword)
    key = input("Enter the key: ")

    while True:
        if BinaryCheck(key):
            break;
        else:
            key = input("Please enter a valid binary for the CRC key: ")

    remainder = modulo2div(codeword, key)
    keylen = len(key)

    if (remainder == "0" * (keylen - 1)):
        print("The transmitted data does not have any error")
        print("The transmitted data is ",codeword[:-(keylen-1)])
    else:
        print("There was an error during transmission.")
except ConnectionRefusedError:
    print("Run the server program first")



    
