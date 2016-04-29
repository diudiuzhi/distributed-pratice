#!/usr/bin/python
import threading


class TransportService:
    def __init__(self, network_service):
        self.network_service = network_service
