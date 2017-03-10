#coding=utf-8


import os
import re

import copy
import shutil
import urllib.request 

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getPngAddr(html):
    png = r"pic/\w+[-]?\w+[-]?\w*\.png"
    tmp = re.compile(png)
    
    html=html.decode('utf-8')#python3
    
    png = re.findall(tmp, html)
    # print png
    for i in range(len(png)):
        png[i] = url + png[i]
    
    return png

def getPngName(pngAddr):
    pngName = copy.deepcopy(pngAddr)
    
    pngT = r'pic/(\w+[-]?\w+[-]?\w*)\.'
    t = re.compile(pngT)
    for i in range(len(pngAddr)):
        pngName[i] = re.findall(t, pngAddr[i])[0]
    
    return pngName
    
def getPng(Addr, Name):
    urllib.request.urlretrieve(Addr, "pic\\%s.png" % Name) 

if __name__=='__main__':
    url = 'http://www.hdb.com/'

    html = getHtml(url)
    print(html)
    pngAddr = getPngAddr(html)
    # print pngAddr
    pngName = getPngName(pngAddr)

    # os.rmdir('pic')
    try:
        shutil.rmtree('pic')
    except WindowsError as e:
        print("couldn't rm folder: no such folder!")
        input("please press Enter to continue > ")
    
    os.mkdir('pic')

    for i in range(len(pngAddr)):
        getPng(pngAddr[i], pngName[i])

# html_code = chardet.detect(html)['encoding']
# sys_code = sys.getfilesystemencoding()
# print "html is encoding by: ", html_code
# print "system is encoding by: ", sys_code
# 锟斤拷锟斤拷锟斤拷锟揭�
# print html.decode(html_code).encode(sys_code)