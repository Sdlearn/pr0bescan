#/usr/bin/env python
#coding=utf-8
from Core.Common import color,logging
import Libs.DNS as DNS

log = logging.getLogger(__name__)

def output(target):
    customHeaders = ['x-powered-by-360wzb',
            'x-powered-by-anquanbao','x-cache','webluker-edge',
            'powered-by-chinacache']
    cnames = ['360wzb','incapdns','aqb.so']
    target.iscdn = False

    color.cprint(1, 'Test CDN for %s'%target.f_domain)
    try:
        color.cprint(1, 'Test CDN for %s with HTTP Header'%target.f_domain)
        if any('cdn' in header for header in target.header):
            target.iscdn = True

        if not target.iscdn:
            flag = set(target.header).intersection(set(customHeaders))
            target.iscdn = True if len(flag) else None

        if not target.iscdn:
            color.cprint(1, 'Test CDN for %s with CNAME'%target.f_domain)
            r = DNS.DnsRequest(target.f_domain, qtype="CNAME", 
                    server=['8.8.8.8'], protocol='tcp', timeout=10)
            res = r.req()
            if len(res.answers) > 0:
                cname = res.answers[0]['data']
                # 值得学习
                if any(cname_str in cname for cname_str in cnames):
                    target.iscdn = True

        if target.iscdn:
            color.cprint(2,'Result %s'%target.iscdn)
    except:
        color.cprint(3,'Test CDN Failed!')
        log.exception('exception')
    
    color.nprint()
