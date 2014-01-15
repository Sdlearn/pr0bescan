#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Core import *

def main():
    target = Pr0beScan()

    # Display Plugin list 
    if args.list:
        print '\n'.join(target.plugins)
    elif args.url:
        color.logo()
        color.cprint(1,'Init Scaning...')
        if not target.probe(args.url):
            color.cprint(3,'Scaning Probe Faild!')
            exit(-1)
        else:
            color.cprint(2, 'Domain: %s'%target.f_domain)
            color.cprint(2, 'IP: %s'%target.ip)
            if 'server' in target.header and len(target.header['server']):
                color.cprint(2, 'Server: %s'%target.header['server'])
            color.nprint()

        plug = 'Plugins.%s'%args.plugin
        # Debug Plugin
        if args.plugin and plug in target.plugins:
            color.cprint(1, 'Debuging Plugin %s'%plug)
            target.plugin(plug)
        else:
            [target.plugin(plug) for plug in target.plugins]

        etime = runtime()
        color.cprint(1,'End Time %1.f secs'%(etime-stime))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
