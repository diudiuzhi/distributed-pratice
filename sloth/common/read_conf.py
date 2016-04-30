#!/usr/bin/python
from oslo.config import cfg


opt_group = cfg.OptGroup(name='cluster', title="example")
simple_opts = [cfg.StrOpt('cluster.name',
                           default=False,
                           help=("test help"))]

CONF = cfg.CONF
CONF.register_group(opt_group)
CONF.register_opts(simple_opts, opt_group)

print CONF.simple.enable
