#/usr/bin/env python
#coding=utf-8
from Core.Common import color,logging
import socket,Queue
from threading import Thread

log = logging.getLogger(__name__)

class tPort(Thread):
    def __init__(self,queue,ip):
        Thread.__init__(self)
        self.queue = queue
        self.ip = ip

    def run(self):
        while not self.queue.empty():
            try:
                port = self.queue.get()
                sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sk.connect((self.ip,port))
                color.cprint(2,'%s %s'%(self.ip,port))
            except:
                continue

def output(target):
    if hasattr(target,'iscdn') and not target.iscdn:

        Ports=[21,22,23,25,80,81,110,135,139,389,443,445,873,1433,1434,1521,2433,3306,3307,3366,3336,3389,5800,5900,7755,8000,8001,8002,8080,8650,8888,8800,9999,22222,22022,27017,28017,33089,43958]

        color.cprint(1,'Scan Port for IP %s..'%target.ip)
        try:
            threadl = []
            threads = 20   #线程数 
            queue=Queue.Queue()

            [queue.put(port) for port in Ports]
            threadl = [tPort(queue,target.ip) for x in xrange(0, threads)]
            [t.start() for t in threadl]
            [t.join() for t in threadl]
        except:
            color.cprint(3,'Scan Port Failed!')
            log.exception('exception')
        
        color.nprint()

