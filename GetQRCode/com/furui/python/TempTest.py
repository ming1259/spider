#coding=utf-8

import urllib
import ssl,stat,shutil
import cookiejar
print(cookiejar.__dict__)


import os, stat
import shutil

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

#shutil.rmtree(directory, onerror=remove_readonly)




ssl._create_default_https_context= ssl._create_unverified_context

foo='abc'

#*for i,ch in range(len(foo)):
#   print (ch,'(%d)' % i)
 
 
 
class Person:
     def __init__(self,name):
         self.name=name
     def sayhello(self):
         print ('my name is:',self.name)
         
p=Person('Tom')
print(p.sayhello())
print(p)