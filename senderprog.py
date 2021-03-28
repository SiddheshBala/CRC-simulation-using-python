import socket
from utilities import *
       
data = input("Enter the data to be transmitted: ")
#BinaryCheck function check whether the entered string is in binary form 
while True:
    if BinaryCheck(data):
        break;
    else:   
        data = input("Please enter a valid binary for the data: ")

key = input("Enter the CRC key: ")
while True:
    if BinaryCheck(key):
        break;
    else:
        key = input("Please enter a valid binary for the CRC key: ")

key_len = len(key)
temp = data + ("0"*(key_len-1))#Appends 0's to the end of the data to be transmitted
codeword = data

print(temp)
checksum = modulo2div(temp, key)#modulo2div function performs Modulo-2 division 
codeword = codeword+checksum#Adds the checksum to the original data
print(codeword)

s = socket.socket()
host = "127.0.0.1"
port = 60003

s.bind((host, port))
s.listen(5)
print("The server has started listening for incoming connections!")
#s.connect((host,port))

connect, address = s.accept()
print(f"Connection from {address} has been established")
connect.sendall(codeword.encode())
#s.sendall(codeword.encode())
#data = s.recv(2048)
#print(data.decode())
s.close()
