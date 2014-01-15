#/usr/bin/env python
#coding=gbk
import json
from Core.Common import color,logging
from Core.Http import get

log = logging.getLogger(__name__)

def output(target):
    api_url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s'%target.ip
    color.cprint(1,'Get Area for IP %s'%target.ip)
    try:
        code,content = get(api_url)
        jsons = json.loads(content)
        color.cprint(2,'%s %s %s %s'%(jsons['data']['country'].encode('gbk'),
            jsons['data']['region'].encode('gbk'),
            jsons['data']['city'].encode('gbk'),
            jsons['data']['isp'].encode('gbk')))
    except:
        color.cprint(3,'Get Area for IP %s Faild!'%target.ip)
        log.exception('exception')
    color.nprint()

