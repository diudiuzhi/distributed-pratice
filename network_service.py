#!/usr/bin/python
import log
log.setup_logger()
import logging

import tcp_server_service
import tcp_client_service
import threadpool

LOG = logging.getLogger(__name__)


class NetworkService:
    def __init__(self):
        self.ip_addr = "10.166.224.163"
        self.port = 5500
        self.tcp_server = tcp_server_service.TcpServerService(self.ip_addr, self.port)
        self.threadpool = threadpool.Threadpool()
        self.tcp_list = {}

        self.listen()
        self.publish()

    def publish(self):
        # read config to know where other nodes are
        # example
        hosts = ["10.166.224.163"]

        for host in hosts:
            self.tcp_client = tcp_client_service.TcpClientService(host, 5500)
            self.tcp_list[host] = self.tcp_client

            LOG.info("Node Discover %s" % host)

            msg_list = ['publish', self.ip_addr, str(self.port)]
            msg = ",".join(msg_list)
            self.tcp_client.send(msg)

    def listen(self):
        self.threadpool.add_job(self.tcp_server.listen)
        LOG.info("Node start to listening at %s:%d" % (self.ip_addr, self.port))

    def send(self):
        pass

    def receive(self):
        pass
