#/usr/bin/env python
#coding=utf-8
from Core.Common import color,logging

log = logging.getLogger(__name__)

def output(target):
    color.cprint(1,'Test Server Exploit %s...'%target.f_domain)

    if 'server' in target.header:
        server = target.header['server'].lower()
        if 'nginx' in server:
            print 'nginx'
        elif 'apache' in server:
            print 'apache'
        elif 'iis' in server:
            print 'iis'
    color.nprint()


