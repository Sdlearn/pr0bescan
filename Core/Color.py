#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

BLACK = '\033[0m'
BLUE  = '\033[34m'
GREEN = '\033[32m'
CYAN  = '\033[36m'
RED   = '\033[31m'
PURPLE= '\033[35m'
YELLOW= '\033[33m'
WHITE = '\033[37m'
GREY  = '\033[38m'

Program = 'Pro0beScan'
Version = 'Beta 3.4'
Author = 'bstaint'
Blog = 'http://www.bstaint.net/'

# 彩色字体打印
class Color:
    def cprint(self,flag = 1,msg = ''):
        if flag == 1:
            sys.stdout.write('%s[*] %s\n'%(YELLOW,msg))
        elif flag == 2:
            sys.stdout.write('%s[+] %s\n'%(GREEN,msg))
        elif flag == 3:
            sys.stdout.write('%s[!] %s\n'%(RED,msg))

    def nprint(self):
        sys.stdout.write('\n')

    def eprint(self):
        sys.stdout.write(BLUE+'Scanner Maybe Error!!!\n')


    def logo(self):
        sys.stdout.write(YELLOW+'''
 ______     _____ _          _____                 
 | ___ \   |  _  | |        /  ___|                
 | |_/ / __| |/' | |__   ___\ `--.  ___ __ _ _ __  
 |  __/ '__|  /| | '_ \ / _ \`--. \/ __/ _` | '_ \ 
 | |  | |  \ |_/ / |_) |  __/\__/ / (_| (_| | | | |
 \_|  |_|   \___/|_.__/ \___\____/ \___\__,_|_| |_|
                              %s %s'''%(Program,Version)+RED+'''
[!] Usage of %s Damage other Computer!!!\n\n'''%Program)


