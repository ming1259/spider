#coding=utf-8
'''
Created on 2017��3��2��

@author: Robin Fan
'''
#! /usr/bin/env python

import urllib2
import urllib
import cookielib
data={"email":"�û���","password":"����"}  #��½�û��������
post_data=urllib.urlencode(data)
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
headers ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
req=urllib2.Request("http://www.renren.com/PLogin.do",post_data)