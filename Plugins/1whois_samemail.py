#/usr/bin/env python
#coding=utf-8
from Core.Common import color,logging
from Core.Ping import tPing
from Core.Http import get
from re import findall
import Queue

log = logging.getLogger(__name__)

def output(target):
    if hasattr(target,'mail'):
        color.cprint(1,'Whois Same Mail %s Domain ...'%target.mail)
        threadl = []
        threads = 5
        queue = Queue.Queue()
        url = 'http://whois.aizhan.com/reverse-whois/?q=%s&t=email'%target.mail
        try:
            code,content = get(url)
            domain_list = findall(r'_blank">(.*?)</a></td>', content)
            if len(domain_list):
                [queue.put(domain) for domain in domain_list if domain != target.n_domain]
                threadl = [tPing(queue,target.ip) for x in xrange(0, threads)]
                [t.start() for t in threadl]
                [t.join() for t in threadl]
        except:
            color.cprint(3,'Whois Same Mail Domain Failed!')
            log.exception('exception')
        
        color.nprint()
