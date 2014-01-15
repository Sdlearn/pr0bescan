#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
import Queue
from Common import *

log = logging.getLogger(__name__)

class tPing(Thread):

    def __init__(self,queue,ip):
        Thread.__init__(self)
        self.queue = queue
        self.ip = ip

    def run(self):
        from Core.Http import ping

        while not self.queue.empty():
            domain = self.queue.get()
            try:
                ip  = ping(domain)
                if ip == self.ip:
                    msg = '%s *'%domain
                # subnets mark *
                elif ip[0:ip.rfind('.')] == self.ip[0:self.ip.rfind('.')]:
                    msg = '%s %s *'%(domain,ip)
                else:
                    msg = '%s %s'%(domain,ip)
                color.cprint(2,msg)
            except:
                log.exception('exception')
                continue
