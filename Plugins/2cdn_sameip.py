#/usr/bin/env python
#coding=utf-8
import re,Queue,json
from threading import Thread
from Core.Common import color,logging
from Core.Http import get
from Core.Ping import tPing

log = logging.getLogger(__name__)

class tThread(Thread):
    def __init__(self,queue,jsons):
        Thread.__init__(self)
        self.queue = queue
        self.jsons = jsons

    def run(self):
        from Core.Http import get
        while not self.queue.empty():
            url = self.queue.get()
            try:
                code,content = get(url)
                self.jsons += json.loads(content)
            except:
                continue

def output(target):
    if hasattr(target,'iscdn') and not target.iscdn:
        apis = {
            'page_url':'http://dns.aizhan.com/index.php?r=index/pages&q=%s'%target.f_domain,
            'list_url':'http://dns.aizhan.com/index.php?r=index/getress&q=%s&page=%d'
        }

        threadl = jsons = []
        threads = 5   # 线程数
        queue=Queue.Queue()
        color.cprint(1,'Find Domain in Same IP for %s..'%target.f_domain)
        try:
            code,content = get(apis['page_url'])
            match = re.search('1/(\d{1,})', content)

            page = int(match.group(1)) if match else 1
            # 多线程翻页获取同IP域名，
            [queue.put(apis['list_url']%(target.f_domain,i)) for i in xrange(1,page+1)]
            threadl = [tThread(queue,jsons) for x in xrange(0, threads)]
            [t.start() for t in threadl]
            [t.join() for t in threadl]

            #Ping IP
            [queue.put(json['domain']) for json in jsons]
            threadl = [tPing(queue,target.ip) for x in xrange(0, threads)]
            [t.start() for t in threadl]
            [t.join() for t in threadl]
        except:
            color.cprint(3,'Find Domain Failed!')
            log.exception('exception')
        
        color.nprint()
