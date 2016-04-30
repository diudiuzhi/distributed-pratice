#!/usr/bin/python
import logging
from oslo.config import cfg

import common.read_conf
#from sloth.common import log

#log.setup_logger()
#LOG = logging.getLogger(__name__)

CONF_PATH = __file__ + "/../../../sloth.conf"
CONF = cfg.CONF
CONF(default_config_files=[CONF_PATH])


class Sloth:

    def __init__(self):
#        LOG.info("Sloth start %s")
        pass


def main():
    Sloth()
