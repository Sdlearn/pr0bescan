#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import split
from urlparse import urlparse

from Http import head,ping
from Common import *

from Libs.pubsuffix import *
from Libs.utils import find_modules
from Libs.utils import import_string

log = logging.getLogger(__name__)

class Pr0beScan:

    header = {}

    def __init__(self):
        self.plugins = find_modules('Plugins', silent=True)

    def plugin(self,name):
        plugin = import_string(name, silent=True)
        plugin.output(self) if plugin else None

    def probe(self,url):
        try:
            urls = urlparse(url)
            if urls.scheme in ['http','https']:
                param = {}
                self.protocol = urls.scheme

                domains = urls.netloc.split(':')

                self.port = int(domains[1]) if len(domains) == 2 else 80
                self.path = split(urls.path)[0] if urls.path != '' else '/'
                self.f_domain = domains[0]
                self.ip = ping(self.f_domain)
                self.code,self.header = head('%s://%s:%s'%(self.protocol,
                    self.f_domain,self.port))

                psl = PublicSuffixList()
                self.n_domain = psl.get_public_suffix(self.f_domain)
                return True
            else:
                return False
        except:
            log.exception('exception')
            return False
