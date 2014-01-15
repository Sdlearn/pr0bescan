#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib,urllib2
from socket import gethostbyname,setdefaulttimeout
setdefaulttimeout(5)

# HEAD请求
def head(url):
    header = {}
    try:
        req = urllib2.Request(url) 
        req.add_header('referer','http://www.google.com.hk/')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36')
        req.get_method = lambda : 'HEAD'
        response = urllib2.urlopen(req)
        code = response.getcode()
        header = response.headers.dict
    except urllib2.URLError, e:
        code = e.code
    return code,header 

# POST请求   
def post(url, data): 
    content = ''
    data = urllib.urlencode(data) 
    try:
        req = urllib2.Request(url,data) 
        req.add_header('referer','http://www.google.com.hk/')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36')
        response = urllib2.urlopen(req) 
        code = response.getcode()
        content = response.read()
    except urllib2.URLError, e:
        code = e.code
    return code,content

# GET请求
def get(url):
    content = ''
    try:
        req = urllib2.Request(url) 
        req.add_header('referer','http://www.google.com.hk/')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36')
        response = urllib2.urlopen(req)
        code = response.getcode()
        content = response.read()
    except urllib2.URLError, e:
        code = e.code
    return code,content

# PING
def ping(domain):
    return gethostbyname(domain)
