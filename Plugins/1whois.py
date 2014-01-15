#/usr/bin/env python
#coding=utf-8
import json
from re import findall
from Core.Common import color,logging,time
from Core.Http import get

log = logging.getLogger(__name__)
    
keywords = ['whoisprivacyprotect','webnic.cc','sudu.cn','markmonitor','godaddy','everdns.com','bizcn.com','whoisprotectionservice','sun-privacy','xinnet.com','zhujiwu.com','west263.com','enom.com','privacyguardian','zgsj.com','1api.net','alibaba-inc.com']

def mail_f(mail):
    return not any(keyword in mail.lower() for keyword in keywords)

def output(target):
    apis = {
            'url1':'http://whois.hichina.com/whois/api_whois?host=%s&oper=1&_=%.3f'%(target.n_domain,time.time()),
            'url2':'http://whois.hichina.com/whois/api_whois_full?host=%s&web_server=%s&_=%.3f',
            'url3':'http://whois.hostsir.com/?domain=%s'%target.n_domain
    }

    color.cprint(1,'Whois %s Domain...'%target.n_domain)
    try:
        mails = False
        try:
            # API1
            code,content = get(apis['url3'])
            mail_l = findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', content)
            mails = filter(mail_f,mail_l) if mail_l else None
        except:
            color.cprint(3,'Get URL %s Faild'%apis['url3'])

        # API2
        if not mails:
            code,content = get(apis['url1'])
            jsons = json.loads(content.decode('gbk'))
            if not 'email' in jsons:
                # 重复4次，该API不稳定
                for i in range(1,3):                    
                    code,content = get(apis['url2']%(target.n_domain,
                        jsons['whois_server'],time.time()))
                    mail_l = findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', content)
                    if mail_l:
                        mails = filter(mail_f,mail_l)
                        break
            else:
                email = jsons['email'].strip()
                if not email in blacklist:
                    mails = [email] 
        # 输出
        if mails:
            target.mail = mails[0].lower()
            color.cprint(2,target.mail)
    except:
        color.cprint(3,'Whois Domain Failed!')
        log.exception('exception')

    color.nprint()
