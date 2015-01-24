'''
Created on 05-Aug-2013

@author: Kashaj
'''
import urllib
#import urllib2
import re
 
uf = urllib.urlopen("http://erail.in/")
t = uf.read()
f = open("we.html",'r+',encoding = 'utf_8')
fout = open("utf8.html",'w')
outbytes = bytearray()
f.write(t)
for line in f:
    for c in line:
        if ord(c) > 127:
            outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
        else: outbytes.append(ord(c))
outstr = str(outbytes,encoding = 'utf_8')
fout.write(outstr)
print(outstr)

        
            
               




