#!/usr/bin/python
import logging


def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        filename='/var/log/node.log')
    logging.basicConfig(format='[%(asctime)s] '+logging.BASIC_FORMAT)
    logging.BASIC_FORMAT = "%(levelname)s:%(name)s:%(message)s"
