#!/usr/bin/python
import socket
import threadpool
import time


class TcpServerService:
    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port = port
        self.socket = self.get_socket()
        self.threadpool = threadpool.Threadpool()

    def get_socket(self):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.bind((self.ip_addr, self.port))
        mysocket.listen(10)
        return mysocket

    def listen(self):
        print "Start to listen"
        while True:
            conn, address = self.socket.accept()
            self.threadpool.add_job(self.dojob, conn, address)

    def send(self):
        pass

    def receive(self):
        pass

    def dojob(self, conn, address):
        while True:
            print "Establish  connected to %s" ,address
            time.sleep(1)
