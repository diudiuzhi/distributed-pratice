#!/usr/bin/python
import socket


class TcpClientService:
    def __init__(self, ip_addr, port):
        self.socket = self.get_socket(ip_addr, port)

    def get_socket(self, ip_addr, port):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.connect((ip_addr, port))
        return mysocket

    def send(self, msg):
        self.socket.sendall(msg)

    def receive(self):
        pass

    def close(self):
        self.socket.close()
