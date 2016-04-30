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
            data_list = conn.recv(1024).split(",")
            if data_list[0] == "publish":
                self.threadpool.add_job(self.discover_node, conn, address)
            if data_list[0] == "node_info":
                self.threadpool.add_job(self.get_node_info)

            time.sleep(1)

    def send(self):
        pass

    def receive(self):
        pass

    def discover_node(self, conn, address):
        print "Establish  connected to %s" % str(address)

    def get_node_info(self):
        print "get node info "
