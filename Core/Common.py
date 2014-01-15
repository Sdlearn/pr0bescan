#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import time
import logging
from Color import *

# 处理参数命令
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', action='store_true',help='Display Plugins List'
            ,dest='list', default=False) 
    parser.add_argument('-d', action='store', help="Debug Plugin"
            ,dest='plugin') 
    parser.add_argument('-u', action='store',help="Target URL",
            dest='url')
    parser.add_argument('-v','--version', action='version',
            version="%s (version %s)"%(Program,Version), 
            help='Print Version Information')
    return parser,parser.parse_args()

def runtime():
    return time.time()

# 彩色字体输出 
color = Color()
# 记录日志
logging.basicConfig(filename = './Cache/debug.log', level = logging.DEBUG)
