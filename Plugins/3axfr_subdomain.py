#/usr/bin/env python
#coding=utf-8
from Core.Common import color,logging
from Core.Http import get,post
from Core.Ping import tPing
from re import findall
import Queue

log = logging.getLogger(__name__)

def output(target):
    if hasattr(target,'axfr') and not target.axfr:
        threadl = []
        threads = 5
        queue = Queue.Queue()

        apis = [{'url':'http://www.baidu.com/s?wd=site:%s&pn=0&ie=utf-8'%target.n_domain,'method':'get','regex':'"g">(.*?)%s'%target.n_domain},
                {'url':'http://i.links.cn/subdomain/','method':'post','regex':'target=_blank>http://(.*)%s','data':{'domain':target.n_domain,'b2':'1','b3':'1','b4':'1'}},
                {'url':'http://www.alexa.com/siteinfo/%s'%target.n_domain,'method':'get','regex':"word-wrap'>(.*?)%s"%target.n_domain}]
        
        color.cprint(1,'Find Subdomain for %s..'%target.n_domain)
        try:
            pix_list = []
            for api in apis:
                try:
                    if api['method'] == 'get':
                        code,content = get(api['url'])
                        pix_list += findall(api['regex'], content)
                    elif api['method'] == 'post':
                        code,content = post(api['url'],api['data'])
                        pix_list += findall(api['regex'], content)
                except:
                    color.cprint(3,'Get %s Faild!'%api['url'])
                    log.exception('exception')

            pix_list = {}.fromkeys(pix_list).keys()

            for pix in pix_list:
                queue.put('%s%s'%(pix,target.n_domain))
            
            threadl = [tPing(queue,target.ip) for x in xrange(0, threads)]
            [t.start() for t in threadl]
            [t.join() for t in threadl]
        except:
            color.cprint(3,'Find Subdomain Failed!')
            log.exception('exception')

        color.nprint()
