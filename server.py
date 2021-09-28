import socket
from threading import Thread
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverip="192.168.56.103"
serverport=1234


clientip = "192.168.237.151"
clientport = 10048

s.bind((serverip,serverport))
print("welcome to chat server".center(60))


def recv():


    while True:
        x=s.recvfrom(1024)
        data=x[0].decode()
        print("\nreceived>> "+data)
        if data == "bye":
            exit()


def send():
    while True:
        string=input("send>> ")
        s.sendto(bytes(string.encode()),(clientip,clientport))


        if string == "bye":
            exit()


Thread(target=recv).start()
Thread(target=send).start()
