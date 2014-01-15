#/usr/bin/env python
#coding=utf-8
from Core.Common import color,logging
import Libs.DNS as DNS
from socket import inet_aton

log = logging.getLogger(__name__)

def valid_ip(address):
    try: 
        inet_aton(address)
        return True
    except:
        return False

def parse_record(records,ip):
    for record in records:
        if valid_ip(record['data']):
            if record['data'] == ip:
                color.cprint(2,'%s *'%(record['name']))
            else:
                color.cprint(2,'%s %s'%(record['name'],record['data']))

def output(target):
    target.axfr = False
    color.cprint(1,'Test AXFR Request for %s'%target.n_domain)
    try:
        # get dns domain
        r = DNS.DnsRequest(target.f_domain, qtype="NS", server=['8.8.8.8'], protocol='tcp', timeout=10)
        res = r.req()
        dns = res.authority[0]['data'][0]
        r = DNS.DnsRequest(target.n_domain, qtype="AXFR", server=[dns], protocol='tcp', timeout=10)
        res = r.req()
        if len(res.answers) > 0:
            target.axfr = True
            parse_record(res.answers,target.ip)
            
    except:
        color.cprint(3,'Test AXFR Failed!')
        log.exception('exception')
    
    color.nprint()
