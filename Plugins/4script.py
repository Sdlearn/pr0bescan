#/usr/bin/env python
#coding=utf-8

from Core.Http import head,get 
from re import search
from Core.Common import color,logging

log = logging.getLogger(__name__)

def output(target):
    powereds = [{'type':'ASP/ASPX','str':'ASP.NET'},
            {'type':'PHP','str':'PHP/'}]

    scripts = [{'type':'ASP','url':'index.asp'},
            {'type':'ASPX','url':'index.aspx'},
            {'type':'PHP','url':'index.php'}]

    searchs = [{'type':'ASP',
        'url':'http://www.google.com.hk/search?q=site:%s+inurl:asp'%target.f_domain},
            {'type':'ASPX',
                'url':'http://www.google.com.hk/search?q=site:%s+inurl:aspx'%target.f_domain},
            {'type':'PHP',
                'url':'http://www.google.com.hk/search?q=site:%s+inurl:php'%target.f_domain}]

    color.cprint(1,'Guess Website %s Script...'%target.f_domain)
    target.script = 'unknown'

    if 'x-powered-by' in target.header:
        color.cprint(1, 'Test Script for %s with X-Powered-By'%target.f_domain)
        for item in powereds:
            if item['str'] in target.header['x-powered-by']:
                target.script = item['type']
                break

    if target.script == 'unknown':
        color.cprint(1, 'Test Script for %s with HTTP Header'%target.f_domain)
        for item in scripts:
            try:
                url = '%s://%s:%s/%s'%(target.protocol,target.f_domain,
                        target.port,item['url'])
                code,header = head(url)
                if code == 200:
                    target.script = item['type']
                    break
            except:
                color.cprint(3,'Head %s Faild!'%item['url'])
                continue

    if target.script == 'unknown':
        color.cprint(1, 'Test Script for %s with Search Engine'%target.f_domain)
        for item in searchs:
            try:
                code,content = get(item['url'])
                match = search(r'resultStats">(.*?)<nobr>', content)
                if match:
                    target.script = item['type']
            except:
                color.cprint(3,'Get %s Faild!'%item['url'])
                continue
    
    color.cprint(2,target.script)
    color.nprint()
        
