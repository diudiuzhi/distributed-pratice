#!/usr/bin/python
import ConfigParser
import time
import sys

#import network_service
#import transport_service

cf = ConfigParser.ConfigParser()
cf.read("../../sloth.conf")


class Node:
    def __init__(self):
        self.node_name = cf.get("node", "node.name")
        print self.node_name
        for s in sys.argv:
            print s
   #     self.network_service = network_service.NetworkService()
  #      self.transport_service = transport_service.TransportService(self.network_service)

 #       while True:
 #           for h in self.network_service.tcp_list:
 #               print h
 #           time.sleep(1)

    def get_node_name(self):
        return self.node_name

    def get_node_id(self):
        return self.node_id


def main():
    Node()

if __name__ == "__main__":
    main()
