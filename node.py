#!/usr/bin/python
import network_service
import transport_service
import time


class Node:
    def __init__(self, node_name, node_id):
        self.node_name = node_name
        self.node_id = node_id
        self.network_service = network_service.NetworkService()
        self.transport_service = transport_service.TransportService(self.network_service)

        while True:
            for h in self.network_service.tcp_list:
                print h
            time.sleep(1)

    def get_node_name(self):
        return self.node_name

    def get_node_id(self):
        return self.node_id


if __name__ == "__main__":
    a = Node("node1", "000001")

    print a.get_node_name()
    print a.get_node_id()
